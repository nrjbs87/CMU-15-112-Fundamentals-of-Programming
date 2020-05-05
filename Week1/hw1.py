#################################################
# hw1.py
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

def isEvenPositiveInt(x):
    if (isinstance(x, int) != True): return False
    elif (x > 0 and x%2 == 0): return True
    else: return False
    
def nearestBusStop(street):
    rem = street % 8
    if rem <= 4: street -= rem
    else: street += (8-rem)
    return street

def isPerfectSquare(n):
    if (isinstance(n, int) != True): return False
    elif(n < 0): return False
    elif (math.sqrt(n)).is_integer(): return True
    else: return False

def nthFibonacciNumber(n):
    n= n+1
    r = ((((1+math.sqrt(5)))**n - ((1-math.sqrt(5)))**n)/((2**n)*math.sqrt(5)))
    return  math.floor(r)

def numberOfPoolBalls(rows):
    return (rows*(rows+1))/2

def isFactorish(n):
    if ((isinstance(n, int) == False) or abs(n) < 102 or abs(n) > 987):
        return False
    elif (n < 0):
        n = abs(n)
    d1 = (n//1) % 10
    d2 = (n//10) %  10
    d3 = (n//100) % 10
    if ((d1==d2 or d2==d3 or d1 == d3) or (d1 == 0 or d2 == 0 or d3 ==0)):
        return False
    elif (n%d1 == 0 and n%d2 == 0 and n%d3 == 0):
        return True
    else:
        return False

def nearestOdd(n):
    rem = n%2
    if rem == 1: return int(n)
    elif rem == 0: return int(n - 1)
    elif rem > 0.5: return int(math.floor(n))
    else: return int(math.ceil(n))

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    x1 = x1
    y1 = y1
    x4 = x1 + w1
    y4 = y1 + h1
    
    x2 = x2
    y2 = y2
    _x4 = x2 + w2
    _y4 = y2 + h2
    
    if (x2 > x4 or _x4 < x1):
        return False
    if (y2 > y4 or _y4 < y1):
        return False
    else:
        return True

def numberOfPoolBallRows(balls):
    return (int(math.ceil((math.sqrt((8*balls)+1) - 1)/2)))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    return 42

def colorBlender(rgb1, rgb2, midpoints, n):
    if (n < 0 or n > (midpoints + 1)):
        return None
    red1 = (rgb1 // 1000000) % 1000
    green1 = (rgb1 // 1000) % 1000
    blue1 = (rgb1 // 1) % 1000

    red2 = (rgb2 // 1000000) % 1000
    green2 = (rgb2 // 1000) % 1000
    blue2 = (rgb2 // 1) % 1000

    delta_red = ((red2 - red1)/(midpoints + 1)) * n
    delta_green = ((green2 - green1)/(midpoints + 1)) * n
    delta_blue = ((blue2 - blue1)/(midpoints + 1)) * n

    new_red = roundHalfUp(delta_red + red1)
    new_green = roundHalfUp(delta_green + green1)
    new_blue = roundHalfUp(delta_blue + blue1)

    return new_red * 10**6 + new_green * 10**3 + new_blue

def playThreeDiceYahtzee(dice):
    return 42

def real(z):
    return (complex(z)).real # since in 2.5 non-complex don't have .real

def findIntRootsOfCubic(a, b, c, d):
    p = -b/(3*a)
    q = p**3 + (b*c-3*a*d)/(6*a**2)
    r = c/(3*a)
    temp = ((q**2)+(r-(p**2))**3)**(1/2)
    x = roundHalfUp(((q+temp)**(1/3)+(q-temp)**(1/3)+p).real)
    temp = (b**2-4*a*c-2*a*b*x-3*a**2*x**2)**(1/2)
    y = roundHalfUp(((-b-x*a+temp)/(2*a)).real)
    z = roundHalfUp(((-b-x*a-temp)/(2*a)).real)
    # Re-order roots in ascending order
    root1 = min(x, y, z)
    root3 = max(x, y, z)
    root2 = (x+y+z)-(root1+root3)
    return root1, root2, root3

#################################################
# Test Functions
#################################################

def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert(isEvenPositiveInt(809) == False)
    assert(isEvenPositiveInt(810) == True)
    assert(isEvenPositiveInt(2389238001) == False)
    assert(isEvenPositiveInt(2389238000) == True)
    assert(isEvenPositiveInt(-2389238000) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')

def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assert(nthFibonacciNumber(0) == 1)
    assert(nthFibonacciNumber(1) == 1)
    assert(nthFibonacciNumber(2) == 2)
    assert(nthFibonacciNumber(3) == 3)
    assert(nthFibonacciNumber(4) == 5)
    assert(nthFibonacciNumber(5) == 8)
    assert(nthFibonacciNumber(6) == 13)
    print('Passed.')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed.')

def testIsFactorish():
    print('Testing isFactorish()...', end='')
    assert(isFactorish(412) == True)      # 4, 1, and 2 are all factors of 412
    assert(isFactorish(-412) == True)     # Must work for negative numbers!
    assert(isFactorish(4128) == False)    # has more than 3 digits
    assert(isFactorish(112) == False)     # has duplicates digits (two 1's)
    assert(isFactorish(420) == False)     # has a 0 (no 0's allowed)
    assert(isFactorish(42) == False)      # has a leading 0 (no 0's allowed)
    assert(isFactorish(1.0) == False)     # floats are not factorish
    assert(isFactorish('nope!') == False) # don't crash on strings
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed.')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def testPlayThreeDiceYahtzee():
    print('Testing playThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(playThreeDiceYahtzee(2312413) == (432, 4))
    assert(playThreeDiceYahtzee(2315413) == (532, 5))
    assert(playThreeDiceYahtzee(2345413) == (443, 18))
    assert(playThreeDiceYahtzee(2633413) == (633, 16))
    assert(playThreeDiceYahtzee(2333413) == (333, 29))
    assert(playThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = findIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # mild
    # testIsEvenPositiveInt()
    # testNearestBusStop()
    # testIsPerfectSquare()
    # testNthFibonacciNumber()
    # testNumberOfPoolBalls()
    # testIsFactorish()
    # testNearestOdd()

    # medium
    # testRectanglesOverlap()
    # testNumberOfPoolBallRows()
    # testThreeLinesArea()

    # spicy
    # testColorBlender()
    # testPlayThreeDiceYahtzee()
    # testFindIntRootsOfCubic()

def main():
    cs112_s20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
