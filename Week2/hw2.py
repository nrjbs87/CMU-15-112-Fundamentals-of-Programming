#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_s20_unit2_linter
import basic_graphics
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

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

#################################################
# Functions for you to write
#################################################

def drawFancyWheels(canvas, width, height, rows, cols):
    return 42

def checkDigits(n, x):
    count = 0
    while (n):
        if(n%10 == x):
            count +=1 
        n = int(n/10)
    return count

def mostFrequentDigit(n):
    if (n<0):
        n = -n
    result = 0
    max_count = 0
    for x in range(10):
        count = checkDigits(n, x)
        if(count > max_count):
            max_count = count
            result = x
    return result
#############################################
def isPrime(n):
    if (n<2):
        return False
    if (n ==2):
        return True
    if (n%2 == 0):
        return False
    max_factor = roundHalfUp(n**0.5)
    for factor in range(3, max_factor+1, 2):
        if (n%factor == 0):
            return False
    return True

def reverseInt(n):
    d = 0
    rev = 0
    temp = n
    while (n>0):
        d = n%10
        n = int(n//10)
        rev = (rev*10) + d
    if (rev == temp):
        return True
    else:
        return False

def nthPalindromicPrime(n):
    guess = 0
    found = 0
    while(found <= n):
        guess +=1
        if(isPrime(guess) and reverseInt(guess)):
            found += 1
    return guess
#############################################
def carrylessAdd(x, y):
    sol, i = 0, 0
    while x or y:       
        var = ((x%10 + y%10)%10)
        sol = var * (10**i) + sol
        x,y,i = int(x/10), int(y/10), i+1
    return sol

def integral(func, a, b, N):
    w = float(b-a)/N
    area = func(a) + func(b)
    if(N == 1):
        return (((func(a) + func(b))/2) * w)
    if(abs(b-a) < N):
        for x in range(1, N):
            area += 2*func(a+(x/N))
    else:
        for x in range(a, b-1):
            area += 2*func(a+x)
    area*=w/2
    return area

def checkEachDigit(n):
    count = 0
    for x in range(10):
        N = n**5
        while(N):
            if(N%10) == x:
                count +=1
                break   
            else:
                N//=10
    if(count == 10):
        return True

def nthWithProperty309(n):
    n = n+1
    found = 0
    guess = -1

    while (found != n):
        guess += 1 
        if (checkEachDigit(guess)):
            found += 1
    return guess

def slideLeft(n, l):
    rest = (n % 10**l)
    leftMost = (n//10**l) % 10
    return rest* 10 + leftMost

def isCircularPrime(n):
    count = 0
    if(n == 0):
        l = 0
    else:
        l = int(math.log10(n))
    if (isPrime(n)): 
        for x in range(l):
            n = slideLeft(n,l)
            if(isPrime(n)!= True):
                break
            else:
                count += 1
    else:
        return False
    if (count == l):
        return True

def nthCircularPrime(n):
    guess = -1
    count = 0
    while(count <= n):
        guess += 1
        if(isCircularPrime(guess)):
            count += 1
    return guess 

def findZeroWithBisection(f, x0, x1, epsilon):

    sign0 = f(x0) > 0
    sign1 = f(x1) > 0

    if(sign0 == sign1):
        return False

    while(abs((x1-x0) > epsilon)):
        x_mp = (x1+x0)/2
        if(f(x_mp)) < sign0: x0 = x_mp
        else: x1 = x_mp   
    return x_mp

def primeFactorsSum(n):
    attempt = 2
    temp = n
    done_dividing = 1
    sum_factors = 0
    last_factor = 1
    while done_dividing!=n:
        if(isPrime(attempt)):
            if(attempt == temp):
                sum_factors = last_factor 
                break
            if(n%attempt == 0):
                n //= attempt
                while(attempt>0):
                    sum_factors += attempt%10
                    last_factor = attempt%10
                    attempt = int(attempt/10)
                attempt = 0
        attempt +=1
    return sum_factors 

def sumDigits(n):
    sumDigitsAttempt = 0
    while (n > 0):
        sumDigitsAttempt += n%10
        n //= 10
    return sumDigitsAttempt

def nthSmithNumber(n):
    n = n+1
    found = 0
    attempt = 4
    while(found < n):
        if(sumDigits(attempt) == primeFactorsSum(attempt)):
            found +=1
        attempt += 1     
    return attempt -1

def carrylessMultiply(x1, x2):
    reset= x1
    num = 0
    sol = 0
    l2 = int(math.log10(x2)) + 1
    l1 = int(math.log10(x1)) + 1
    for i in range(l2):
        d2 = x2 % 10
        x2 //= 10
        for j in range(l1):
            d1 = x1%10
            x1 //= 10 
            num = 10**j * ((d2*d1)%10) * (10**i) + num
        sol = carrylessAdd(sol, num)
        num = 0
        x1 = reset
    return sol

def isKazrekarNumber(n):
    if (n==1):
        return True
    sq_n = n*n 
    num_digits = int(math.log10(sq_n)) + 1
    i = 0
    while(i != num_digits):
        i += 1
        multiplier = (int) (pow(10, i))
        if multiplier == n:
            return False
        sum = sq_n//multiplier + sq_n % multiplier 
        if(sum == n):
            return True
    return False

def nthKaprekarNumber(n):
    n = n+1
    found = 0
    attempt = 0

    while(found < n):
        attempt += 1
        if(isKazrekarNumber(attempt)):
            found += 1
    return attempt

def genCarolPrime(n):
    if(n ==0):
        return 7

    return (((2**n - 1)**2) - 2)

def nthCarolPrime(n):
    n = n+1
    found = 0
    attempt = 0
    while (found < n):
        attempt += 1
        cp_attempt = genCarolPrime(attempt)
        if(isPrime(cp_attempt)):
            found += 1
    return cp_attempt

def play112(game):
    return 42

############################
# integerDataStructures
# If you do this spicy problem,
# place your solutions here!

def intCat(sign, count_count, count, n):
    sol = carrylessAdd(count* pow(10, count), n)
    sol = carrylessAdd(sol, (count_count* pow(10, count+count_count)))
    sol = carrylessAdd(sol, (sign* pow(10, count+1+count_count)))
    return int(sol)

def lengthEncode(n):
    if(n<0): 
        sign = 2 
        n=-n
    else: sign = 1

    if(n==0): count = 1
    else: count = int(math.log10(n))+1

    if(count<=9): count_count = 1
    else: count_count = 2

    return(intCat(sign, count_count, count, n))

def lengthDecode(n):

    length = int(math.log10(n) + 1)

    # retrieve sign and adjust n
    sign = int(n//pow(10,length-1))
    if(sign ==2):sign = -1
    n = int(n%pow(10, length-1))

    # retrieve cc and adjust n
    cc = int(n//pow(10,length-2))
    n = int(n%pow(10, length-2))

    # retrieve count and adjust n
    if(cc == 1):
        count = int(n//pow(10,length-3))
        n = int(n%pow(10, length-3))
    else:
        count = int(n//pow(10,length-4))
        n = int(n%pow(10, length-4))

    print(sign,cc, count, n)

    return n*sign

def lengthDecodeLeftmostValue(n):

    length = int(math.log10(n) + 1)

    # retrieve sign and adjust n
    sign = int(n//pow(10,length-1))
    if(sign ==2):sign = -1
    n = n%pow(10, length-1)
    n = int(n)

    # retrieve cc and adjust n
    cc = int(n//pow(10,length-2))
    n = int(n%pow(10, length-2))

    # retrieve count and adjust n
    if(cc == 1):
        count = int(n//pow(10,length-3))
        n = int(n%pow(10, length-3))
        sub = 3
    else:
        count = int(n//pow(10,length-4))
        n = int(n%pow(10, length-4))
        sub = 4
    
    # retrieve n and adjust rest
    sol = int(n//pow(10, length-sub-count))
    rest = int(n%pow(10, length-sub-count)) 
    return sol, rest

#########################################################################
# Begin Lists Functions

def newIntList():
    return 1110

def intListLen(n):
    if (n == 1110):
        left_most = 0
    else:
        length = int(math.log10(n) + 1)

        # retrieve sign and adjust n
        sign = int(n//pow(10,length-1))
        if(sign ==2):sign = -1
        n = int(n%pow(10, length-1))

        # retrieve cc and adjust n
        cc = int(n//pow(10,length-2))
        n = int(n%pow(10, length-2))

        # retrieve count and adjust n
        if(cc == 1):
            count = int(n//pow(10,length-3))
            n = int(n%pow(10, length-3))
            sub = 3
        else:
            count = int(n//pow(10,length-4))
            n = int(n%pow(10, length-4))
            sub = 4
        left_most = int(n//pow(10, length-sub-count))

    return left_most

def intListGet(L, i):
    num_items,L = lengthDecodeLeftmostValue(L)
    if (i > (num_items-1)):
        return 'index out of range'
    if(L == 1110):
        return 'index out of range'
    for x in range(i+1):
        sol, rem = lengthDecodeLeftmostValue(L)
        L = rem

    return(sol)

def intListSet(L,i,v):

    # find length of number you want to remove
    # find length of number you want to add
    # add delta to lenth(L) for monitoring how many zeros
    
    # remove the length from L
    num_items = intListLen(L)

    if (i >= num_items or i < 0): 
        return 'index out of range'
    else:
        # understand how long the number we're removing is
        num_remove = intListGet(L, i)
        print("num_remove:", num_remove)
        length_remove = int(math.log10(lengthEncode(num_remove)) + 1)
        
        L = int(L%pow(10, int(math.log10(L) -3)))

        # understand how long the number we're adding it
        num_add = lengthEncode(v)
        length_add = int(math.log10(num_add) + 1)
        print("num_add:", num_add)

        # solify how many zeros should be in your solution 
        delta = length_add - length_remove 
        L_length = int(math.log10(L)) + 1
        # remove 4 to remove the digits used to store length
        # added -1 but not sure!
        num_zeros = L_length + delta 
        
        num_zeros_temp = num_zeros 
        v = lengthEncode(v)
        v_length = int(math.log10(v)) + 1
        newL = 0 * pow(10, num_zeros-4)
        for x in range(num_items):
            sol, rem = lengthDecodeLeftmostValue(L)
            L = rem
            if(x == i): 
                num_zeros -= v_length 
                newL = v *  pow(10, num_zeros) + newL
            else:
                sol_length = int(math.log10(lengthEncode(sol))) + 1
                num_zeros -= sol_length 
                newL = lengthEncode(sol) * pow(10, num_zeros) + newL
    newL_length = int(math.log10(newL)+1)
    return int((newL + pow(10, num_zeros_temp) * lengthEncode(num_items)))

def intListAppend(L,v):
    v = lengthEncode(v)
    v_length = int(math.log10(v)) + 1

    if(L == 1110): return int(1111 * pow(10, v_length) + v)
    else:
        num_items = intListLen(L)
        L = int(L%pow(10, int(math.log10(L) -3)))
        L_length = int(math.log10(L)) + 1

        L = L * pow(10, v_length) + v

        new_num_items = num_items + 1
        new_L_length = int(math.log10(L)) + 1

        return int(lengthEncode(new_num_items) * pow(10, new_L_length) + L)

def intListPop(L):
    num_items,L = lengthDecodeLeftmostValue(L)
    tempL = L
    new_num_items = num_items - 1

    for x in range(num_items):
        sol, rem = lengthDecodeLeftmostValue(L)
        L = rem
    length_remove = int(math.log10(lengthEncode(sol)) + 1)
    L = tempL//pow(10, length_remove)
    L_length = int(math.log10(L)+1)
    return int(pow(10,L_length)*lengthEncode(new_num_items)+L),sol
#########################################################################
# Begin Sets Functions

def newIntSet():
    return 1110

def intSetAdd(s, v):
    v = lengthEncode(v)
    v_length = int(math.log10(v)) + 1
    
    num_items, s = lengthDecodeLeftmostValue(s)
    s_temp = s

    if(s == 1110): return int(1111 * pow(10, v_length) + v)

    for x in range(num_items):
        sol, rem = lengthDecodeLeftmostValue(s)
        s = rem
        if(lengthEncode(sol) == v):
            return int(lengthEncode(num_items) * pow(10, 5) + s_temp )
    
    s = int(s_temp * pow(10, v_length) + v)
    new_num_items = num_items + 1
    new_s_length = int(math.log10(s)) + 1
    return (int(lengthEncode(new_num_items) * pow(10, new_s_length)) + s)

def intSetContains(s, v):
    v = lengthEncode(v)
    v_length = int(math.log10(v)) + 1
    num_items, s = lengthDecodeLeftmostValue(s)

    for x in range(num_items):
        sol, rem = lengthDecodeLeftmostValue(s)
        s = rem
        if(lengthEncode(sol) == v):
            return True
    return False
##########################################################################
# Start Maps Functions

def newIntMap():
    return 1110

def intMapContains(m, key):
    num_items, m = lengthDecodeLeftmostValue(m)
    for x in range(num_items//2):
        for y in range(0,1):
            key_, rem = lengthDecodeLeftmostValue(m)
            m = rem
            value, rem = lengthDecodeLeftmostValue(m)
            m = rem
            if(key_ == key): return True
    return False

def intMapGet(m, key):
    num_items, m = lengthDecodeLeftmostValue(m)
    for x in range(num_items//2):
        for y in range(0,1):
            key_, rem = lengthDecodeLeftmostValue(m)
            m = rem
            value, rem = lengthDecodeLeftmostValue(m)
            m = rem
            if(key_ == key): return value
    return 'no such key'

def intMapSet(m, key, value):
    if intMapContains(m, key) == True: # replace value if key exists
        num_remove = intMapGet(m, key)
        num_remove_length = int(math.log10(lengthEncode(num_remove))) + 1
        num_items, m = lengthDecodeLeftmostValue(m)
        m_length = int(math.log10(m)) + 1
        num_add_length = int(math.log10(lengthEncode(value))) + 1
        delta = num_add_length - num_remove_length
        num_zeros = m_length + delta
        sol = 0
        for x in range(num_items//2):
            # key_ is determined here
            key_, rem = lengthDecodeLeftmostValue(m)
            m = rem
            # value_ is determined here
            num_zeros -= int(math.log10(lengthEncode(key_))) + 1
            sol += lengthEncode(key_) * pow(10,num_zeros)
            length_key = int(math.log10(lengthEncode(key_))) + 1
            if(key == key_):
                value_, rem = lengthDecodeLeftmostValue(m)
                value_ = value
                num_zeros -= int(math.log10(lengthEncode(value_))) + 1
                m = rem
                sol += lengthEncode(value_) * pow(10, num_zeros)
            else:
                value_, rem = lengthDecodeLeftmostValue(m)
                num_zeros -= int(math.log10(lengthEncode(value_))) + 1
                m = rem
                sol += lengthEncode(value_) * pow(10, num_zeros)
        sol_length = int(math.log10(sol)) + 1
        return (sol) + pow(10, sol_length) * lengthEncode(num_items)
                
    else: # append key and value if doesn't exist
        length_value = int(math.log10(lengthEncode(value))) + 1
        num_items, m = lengthDecodeLeftmostValue(m)
        m_temp = m
        new_num_items = num_items + 2
        append_this=lengthEncode(key)*pow(10,length_value)+lengthEncode(value)
        length_append = int(math.log10(append_this)) + 1
        sol = m_temp * pow(10, length_append) + append_this
        length_sol = int(math.log10(sol)) + 1
        sol = lengthEncode(new_num_items) * pow(10, length_sol) + sol
        return sol 
#################################################
# Test Functions
# ignore_rest (tell autograder to ignore everything below here)
#################################################

def testDrawFancyWheels():
    print('Testing drawFancyWheels()... (confirm visually)')
    print('  drawFancyWheels: 1 row x 1 col, win size of 400x400...', end='')
    basic_graphics.run(1, 1, width=400, height=400, drawFn=drawFancyWheels)
    print('  drawFancyWheels: 4 rows x 6 cols, win size of 900x600...', end='')
    basic_graphics.run(4, 6, width=900, height=600, drawFn=drawFancyWheels)

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNthWithProperty309():
    print('Testing nthWithProperty309()... ', end='')
    assert(nthWithProperty309(0) == 309)
    assert(nthWithProperty309(1) == 418)
    assert(nthWithProperty309(2) == 462)
    assert(nthWithProperty309(3) == 474)
    print("Passed!")

def testNthCircularPrime():
    print('Testing nthCircularPrime()...', end='')
    # [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113,
    #  131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, ...]
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(20) == 719)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNthCarolPrime():
    print("Testing nthCarolPrime()...", end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    assert(nthCarolPrime(8) == 68718952447)
    assert(nthCarolPrime(9) == 274876858367)
    print("Passed!")

def testPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length-encoded 0
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # [1, 42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # [1, 567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # [2, 9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # [1, 9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # [ 0 ]
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # [ 1, 42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # [ 0 ]
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # [ 2, 42, 73 ]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # [ 2, 42, 98765 ]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # [ 4, 42, 98765, 99, 0 ]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # [ empty stateMap, empty startStateSet ]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # 6* -> 1
    fsm = setTransition(fsm, 1, 7, 2) # 7 -> 2
    fsm = setTransition(fsm, 2, 7, 2) # 7* -> 2
    fsm = setTransition(fsm, 2, 8, 3) # 7* -> 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # [1, 65]
    assert(encodeString('f') == 1111113102) # [1, 102]
    assert(encodeString('3') == 111111251) # [1, 51]
    assert(encodeString('!') == 111111233) # [1, 33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # [4,65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    # testIntFSM()
    # testAccepts()
    # testEncodeDecodeStrings()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # required
    # testDrawFancyWheels()

    # mild
    # testMostFrequentDigit()
    # testNthPalindromicPrime()
    # testCarrylessAdd()
    # testIntegral()
    # testNthWithProperty309()
    # testNthCircularPrime()

    # medium
    # testFindZeroWithBisection()
    # testNthSmithNumber()
    # testCarrylessMultiply()
    # testNthKaprekarNumber()
    # testNthCarolPrime()

    # spicy
    # testPlay112()
    testIntegerDataStructures()

def main():
    cs112_s20_unit2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
