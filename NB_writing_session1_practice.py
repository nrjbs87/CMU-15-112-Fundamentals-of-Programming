#################################################
# writing_session1_practice.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_s20_week1_linter
import math

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

def distance(x1, y1, x2, y2):
    distance = float(math.sqrt(((x2 - x1) **2) + ((y2 - y1) **2)))
    return distance 

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return (distance(x1, y1, x2, y2) <= r1+r2)
 
def getInRange(x, bound1, bound2):
    minVal = min(bound1, bound2)
    maxVal = max(bound1, bound2)

    if x < minVal:
        return minVal
    elif x > maxVal:
        return maxVal
    else:
        return x 

def isFactor(f, n):
    if (n == f): return True
    elif f==0: return False
    elif n%f == 0: return True
    else: return False

def getKthDigit(n, k):
 
    return (abs(n // 10 ** k) % 10)

def setKthDigit(n, k, d):
    if (n < 0):
        return (n + (getKthDigit(n, k)*10**k) - d*10**k)
    else:
        return (n - (getKthDigit(n, k)*10**k) + d*10**k)

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed.')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed.')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed.')

def testIsFactor():
    print('Testing isFactor()... ', end='')
    assert(isFactor(1,1) == True)
    assert(isFactor(2,10) == True)
    assert(isFactor(-5,25) == True)
    assert(isFactor(5,0) == True)
    assert(isFactor(0,0) == True)
    assert(isFactor(2,11) == False)
    assert(isFactor(10,2) == False)
    assert(isFactor(0,5) == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testIsFactor()
    testGetKthDigit()
    testSetKthDigit()
    return None

def main():
    cs112_s20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
