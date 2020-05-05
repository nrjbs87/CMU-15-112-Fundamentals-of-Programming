#################################################
# hw9.py
#
# Your name: Raj Basu
# Your andrew id: neerajb
#
# Names and andrew id's of up to 3 collaborators:
#   name + andrew id #1:
#   name + andrew id #2:
#   name + andrew id #3:
#################################################

import cs112_s20_unit9_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def alternatingSum(L, multi=1):
    if len(L) % 2 == 0:
        multi = -1
    if len(L) == 0:
        return 0
    else: 
        return (L[0] * multi) + alternatingSum(L[1:])

def removeOddDigits(n):
    if n == 0:
        return 0
    elif (n % 10) % 2 != 0:
        return removeOddDigits(n//10) 
    else:
        sol = n % 10 + removeOddDigits(n//10) * 10
        return sol

def onlyEvenDigits(L):
    if L == []:
        return []
    elif len(L) == 0:
        return L  
    elif isinstance(L[0], int):
        return [removeOddDigits(L[0])] + onlyEvenDigits(L[1:])
    else:
        return [removeOddDigits(L[0])] + onlyEvenDigits(L[1:])  

def powersOf3ToN(n):
    L = []
    return powersOf3ToNWrapper(n, L)

def powersOf3ToNWrapper(n, L, base = 3):
    if n < 0:
        return []
    else:
        nextVal = n/base
        logVal = base ** int(math.floor(math.log(n, base)))
        if logVal <= 1:
            L.insert(0, int(logVal))
            return L
        else:
            L.insert(0, int(logVal))
            return powersOf3ToNWrapper(nextVal, L)

def binarySearchValues(L, item):
    lo = 0
    hi = len(L) - 1
    sol = []
    return binarySearchValuesWrapper(L, item, lo, hi, sol)

def binarySearchValuesWrapper(L, item, lo, hi, sol):
    if hi < lo:
        return sol
    else:
        midPoint = lo + (hi - lo) // 2
        if L[midPoint] == item:
            sol.append((midPoint, L[midPoint]))
            return sol
        elif L[midPoint] > item:
            sol.append((midPoint, L[midPoint]))
            hi = midPoint - 1
            return binarySearchValuesWrapper(L, item, lo, hi, sol)
        else:
            sol.append((midPoint, L[midPoint]))
            lo = midPoint + 1
            return binarySearchValuesWrapper(L, item, lo, hi, sol)

def secondLargest(L):
    if len(L) < 2:
        return None

    largest = L[0]
    secondLargest = L[1]
    index = 2

    if (secondLargest > largest):
        largest, secondLargest = secondLargest, largest
    return secondLargestWrapper(L, index, largest, secondLargest)

def secondLargestWrapper(L, index, largest, secondLargest):

    if index > len(L)-1 :
        return secondLargest
    elif L[index] > largest:
        temp = largest
        largest = L[index]
        secondLargest = temp
        return secondLargestWrapper(L, index+1, largest, secondLargest)
    elif L[index] > secondLargest:
        secondLargest = L[index]
        return secondLargestWrapper(L, index+1, largest, secondLargest)
    else:
        return secondLargestWrapper(L, index+1, largest, secondLargest)

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

def testSecondLargest():
    print('Testing secondLargest()...', end='')
    assert(secondLargest([1,2,3,4,5]) == 4)
    assert(secondLargest([4,3]) == 3)
    assert(secondLargest([4,4,3]) == 4)
    assert(secondLargest([-3,-4]) == -4)
    assert(secondLargest([4]) == None)
    assert(secondLargest([ ]) == None)
    print('Passed!')

def testOnlyEvenDigits():
    print('Testing onlyEvenDigits()...', end='')
    assert(onlyEvenDigits([43, 23265, 17, 58344]) == [4, 226, 0, 844])
    assert(onlyEvenDigits([ ]) == [ ])
    print('Passed!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(27) == [1, 3, 9, 27])
    assert(powersOf3ToN(26.999) == [1, 3, 9])
    assert(powersOf3ToN(-1) == [ ])
    print('Passed!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') ==
           [(2, 'f'), (0, 'a'), (1, 'c')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'n') ==
           [(2, 'f'), (4, 'm'), (5, 'q')])
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    print()
    print('Testing **** non-spicy *** hw9 problems!')
    print()

    # mild+medium problems:
    testAlternatingSum()
    testOnlyEvenDigits()
    testPowersOf3ToN()
    testBinarySearchValues()
    testSecondLargest()

    # spicy problems:  NOT HERE!!!
    pass

def main():
    cs112_s20_unit9_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
