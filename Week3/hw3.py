#################################################
# hw3.py
#
# Your name: Raj Basu
# Your andrew id: neerajb
#################################################

import cs112_s20_unit3_linter
import string, random

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

# takes a string of data and returns the sum of scores and the name associated
# returns none if the string is empty 
def calcScore(data):
    score = 0
    name = ''
    for value in data.split(','):
        if value.isdigit(): score += int(value)
        else: name = value
    return name, score

# returns the name of the winner with the highest score returned from calcScore
# returns the names of the individuals in the order they were inputed if a tie
def topScorer(data):
    topScorer = ''
    if (data == ''): return None
    lines = data.splitlines()
    name1, score1 = calcScore(lines[0])
    name2, score2 = calcScore(lines[1])

    if(score1 == score2):
        return name1 + ',' + name2
    
    max_score = max(score1, score2)
    if(max_score == score1): topScorer = name1
    else: topScorer = name2 
   
    return topScorer

# takes a line from text, removes all leading/trailing spaces
# then replaces any remaining spaces with a dash
def removeSpaces_addDashes(line):
    stripped_line = line.strip()
    stripped_dashed_line = stripped_line.replace(" ", "-")

    return stripped_dashed_line
    
# iterates through string, and wraps it at length width
# passes that line to removeSpaces_addDashes
# returns concatenation of resulting strings
def wordWrap(text, width):
    sol = ''
    line = ''
    count = 0
    for c in text:
        line += c
        count +=1
        if(width == len(text)):
            return text
        if(count == len(text)):
            sol += removeSpaces_addDashes(line)
        if(len(line) == width):
            sol += removeSpaces_addDashes(line)
            line = ''
            sol += '\n'
    return sol

# return reveresed string
def reverseString(s):
    revS = s[::-1]
    return revS

# returns true if string is palindrome 
def isPalindrome(s):
    return reverseString(s) == s

# iterates through all possible strings
# returns longest sub palindrome 
def longestSubpalindrome(s):
    L = len(s)
    longestPal = ' '

    if len(s) == 1:
        longestPal = s
    for i in range(L):
        for j in range(0, i):
            attempt = (s[j:i+1])
            if isPalindrome(attempt):
                if(attempt > longestPal):
                    longestPal = attempt
    return longestPal


def mastermindScore(target, guess):
    L_target = len(target)
    L_guess = len(guess)
    exact = 0
    partial = 0
    for i in range(L_target):
        if target[i] == guess[i]:
            exact +=1
            target = target.replace(target[i], " ")
    for i in range(L_target):
        for j in range(L_guess):
            if target[i] == guess[j] and i != j:
                partial +=1
                target = target.replace(target[i], " ")

    if exact  == len(target):
        exact_string = "You win!!!" 
        partial_string = ""

    elif exact > 1 and partial == 0: 
        exact_string = str(exact)+ " exact matches" 
        partial_string = "" 

    elif exact == 0 and partial > 1: 
        exact_string = ""
        partial_string = str(partial)+ " partial matches"

    elif exact == 1 and partial == 0: 
        exact_string = str(exact)+ " exact match" 
        partial_string = "" 

    elif exact == 0 and partial == 1: 
        exact_string = ""
        partial_string = str(partial)+ " partial match"  

    elif exact == 0 and partial == 0: 
        exact_string = "No matches" 
        partial_string = ""

    elif exact == 1 and partial == 1: 
        exact_string = "1 exact match, " 
        partial_string = "1 partial match" 

    elif exact >= 1 and partial == 1: 
        exact_string = str(exact) + " exact matches, " 
        partial_string = str(partial) + " partial match" 

    elif exact == 1 and partial >= 1: 
        exact_string = str(exact) + " exact match, " 
        partial_string = str(partial) + " partial matches" 

    elif exact >= 1 and partial >= 1: 
        exact_string = str(exact) + " exact matches, " 
        partial_string = str(partial) + " partial matches" 

    return exact_string + partial_string

def playPoker(deck, players):
    return 42

def encodeRightLeftRouteCipher(text, rows):
    return 42

def decodeRightLeftRouteCipher(cipher):
    return 42

def topLevelFunctionNames(code):
    return 42

def getEvalSteps(expr):
    return 42

def bonusEncode1(msg):
    return 42

def funDecode1(msg):
    return 42

def bonusEncode2(msg):
    return 42

def funDecode2(msg):
    return 42

def bonusEncode3(msg):
    return 42

def funDecode3(msg):
    return 42

#################################################
# Test Functions
#################################################

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def testWordWrap():
    print('Testing wordWrap()...', end='')
    assert(wordWrap("abc", 3) == "abc")
    assert(wordWrap("abc",2) == "ab\nc") 
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg",  4)  ==  """\
a-b
c-de
fg""")
    print('Passed!')

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')
    print("Passed!'")

def testPlayPoker():
    print('Testing playPoker()...', end='')
    assert(playPoker('QD-3S', 1) == 'Player 1 wins with a high card of QD')
    assert(playPoker('QD-QC', 1) == 'Player 1 wins with a pair to QD')
    assert(playPoker('QD-JS', 1) == 'Player 1 wins with a straight to QD')
    assert(playPoker('TD-QD', 1) == 'Player 1 wins with a flush to QD')
    assert(playPoker('QD-JD', 1) == 'Player 1 wins with a straight flush to QD')
    assert(playPoker('QD-JD', 2) == 'Not enough cards')

    assert(playPoker('AS-2H-3C-4D', 2) ==
                                    'Player 2 wins with a high card of 4D')
    assert(playPoker('5S-2H-3C-4D', 2) ==
                                    'Player 1 wins with a high card of 5S')
    assert(playPoker('AS-2H-3C-2D', 2) == 'Player 2 wins with a pair to 2H')
    assert(playPoker('3S-2H-3C-2D', 2) == 'Player 1 wins with a pair to 3S')
    assert(playPoker('AS-2H-2C-2D', 2) == 'Player 1 wins with a straight to 2C')
    assert(playPoker('AS-2H-2C-3D', 2) == 'Player 2 wins with a straight to 3D')
    assert(playPoker('AS-2H-4S-3D', 2) == 'Player 1 wins with a flush to 4S')
    assert(playPoker('AS-2H-4S-3H', 2) ==
                                    'Player 2 wins with a straight flush to 3H')
    assert(playPoker('2S-2H-3S-3H', 2) ==
                                    'Player 1 wins with a straight flush to 3S')

    assert(playPoker('AS-2D-3C-4C-5H-6D-7S-8D', 2) ==
                                    'Player 2 wins with a high card of 4C')
    assert(playPoker('AS-2D-3S-4C-5H-6D-7S-8D', 4) ==
                                    'Player 3 wins with a flush to 7S')
    print('Passed!')

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

def testFunDecoder(encodeFn, decodeFn):
    s1 = ''
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(' \n\n') + random.choice(string.digits)
    for s in ['a', 'abc', s1]:
        if (decodeFn(encodeFn(s)) != s):
            raise Exception(f'Error in {decodeFn.__name__} on {repr(s)}')
    return True

def testFunDecoders():
    print('Testing funDecoders()...', end='')
    testFunDecoder(bonusEncode1, funDecode1)
    testFunDecoder(bonusEncode2, funDecode2)
    testFunDecoder(bonusEncode3, funDecode3)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # required
    testTopScorer()

    # mild
    testWordWrap()
    testLongestSubpalindrome()

    # # medium
    testMastermindScore()
    # testPlayPoker()

    # # spicy
    # testEncodeAndDecodeRightLeftRouteCipher()
    # testTopLevelFunctionNames()
    # testGetEvalSteps()
    # testFunDecoders()

def main():
    cs112_s20_unit3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
