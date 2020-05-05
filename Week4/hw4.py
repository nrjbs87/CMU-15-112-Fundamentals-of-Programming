#################################################
# hw4.py
#
# Your name: Raj Basu
# Your andrew id: neerajb
#################################################

import cs112_s20_unit4_linter
import basic_graphics
import string, copy, random, math

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

#################################################
# Person class
#################################################

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendsList = [ ]
        self.nameList = [ ]

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def addFriend(self, friend):
        if friend not in self.friendsList: 
            self.friendsList.append(friend)
            friend.friendsList.append(self)
            self.nameList.append(friend.name)
            friend.nameList.append(self.name)

    def addFriends(self, friends):
        for name in friends.friendsList:
            if name not in self.friendsList:
                self.friendsList.append(name)
                self.nameList.append(name.name)
            
    def getFriends(self):
        return self.friendsList
    
    def getFriendsNames(self):
        return sorted(self.nameList)

#################################################
# removeEvens
#################################################

def destructiveRemoveEvens(L): # no return value
    indexs = []
    for i in L:
        if i % 2 == 0:
            indexs.append(i)
    for i in indexs:
        L.remove(i)

def nondestructiveRemoveEvens(L):
    Lcopy = []
    for i in L:
        if i % 2 != 0:
            Lcopy.append(i)
    return Lcopy

#################################################
# bestScrabbleScore
#################################################

def bestScrabbleScore(dictionary, letterScores, hand):
    return 42

#################################################
# solvesCryptarithm
#################################################

def stringToNumber(word, key):
    sol = 0
    L = len(word)-1
    for i in range(len(word)):
            value = key.index(word[i])
            sol += (value * 10 ** (L-i))
    return sol

def solvesCryptarithm(puzzle, solution):
    for letter in puzzle:
        if (letter.isalpha() and letter not in solution):
            return False
            
    wordList = puzzle.split(' ')
    word1 = stringToNumber(wordList[0], solution)
    word2 = stringToNumber(wordList[2], solution)
    word3 = stringToNumber(wordList[4], solution)

    if word1 + word2 == word3: return True
    else: return False
    
#################################################
# drawLetterTypePieChart(canvas)
#################################################

def drawLetterTypePieChart(canvas, text, cx, cy, r):
    return 42

#################################################
# spicy combinatorics problems
#################################################

def allSublists(L):
    yield 42

def solveSubsetSum(L):
    return 42

def heapsAlgorithmForPermutations(L):
    # from https://en.wikipedia.org/wiki/Heap%27s_algorithm
    yield 42

def solveCryptarithmWithMaxDigit(puzzle, maxDigit):
    return 42

def getAllSingletonCryptarithmsWithMaxDigit(words, maxDigit):
    return 42

#################################################
# spicy runSimpleProgram
#################################################

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    #       are the friends of this person, listed in the order that
    #       they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    #       names of the friends of this person.  This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])

    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])

    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

def _destructiveRemoveEvens(L):
    destructiveRemoveEvens(L)
    return L

def testDestructiveRemoveEvens():
    print("Testing destructiveRemoveEvens()...", end="")
    assert(_destructiveRemoveEvens([1,2,3,4]) == [1,3])
    assert(_destructiveRemoveEvens([1,3,5,7,3]) == [1,3,5,7,3])
    assert(_destructiveRemoveEvens([2,4,2,4,6]) == [ ])
    assert(_destructiveRemoveEvens([2,4,1,2,4,6]) == [1])
    print("Passed!")

def _verifyRemoveEvensIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    nondestructiveRemoveEvens(a) # ignore result, just check if destructive
    return (a == b)

def testNondestructiveRemoveEvens():
    print("Testing nondestructiveRemoveEvens()...", end='')
    assert(_verifyRemoveEvensIsNondestructive())
    assert(nondestructiveRemoveEvens([1,2,3,4]) == [1,3])
    assert(nondestructiveRemoveEvens([1,3,5,7,3]) == [1,3,5,7,3])
    assert(nondestructiveRemoveEvens([2,4,2,4,6]) == [ ])
    assert(nondestructiveRemoveEvens([2,4,1,2,4,6]) == [1])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY--ENDRS") == 
                                  True)
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER + NUMBER = PUZZLE", "UMNZP-BLER") ==
                                  True)
    assert(solvesCryptarithm("TILES + PUZZLES = PICTURE", "UISPELCZRT") ==
                                  True)
    assert(solvesCryptarithm("COCA + COLA = OASIS", "LOS---A-CI") ==
                                  True)
    assert(solvesCryptarithm("CROSS + ROADS = DANGER", "-DOSEARGNC") ==
                                  True)

    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND + MORE = MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND + MORE = MONEY","MOY--ENDRS") == False)
    print("Passed!")

def drawLetterTypePieCharts(canvas, width, height):
    r = min(width,height)*0.2
    canvas.create_line(width/2, 0, width/2, height)
    canvas.create_line(0, height/2, width, height/2)
    drawLetterTypePieChart(canvas, "AB, c de!?!", width/4, height/4, r)
    drawLetterTypePieChart(canvas, "AB e", width/4, height*3/4, r)
    drawLetterTypePieChart(canvas, "A", width*3/4, height/4, r)
    drawLetterTypePieChart(canvas, "               ", width*3/4, height*3/4, r)

def testDrawLetterTypePieChart():
    print('Testing drawLetterTypePieChart()...')
    basic_graphics.run(drawFn=drawLetterTypePieCharts, width=800, height=800)
    print('Do a visual inspection to verify this passed!')

def testAllSublists():
    print('  Testing allSublists()...', end='')
    def f(): yield 42
    assert(type(allSublists([1,2,3])) == type(f())) # generator
    assert(sorted(allSublists([1])) == [ [], [1] ])
    assert(sorted(allSublists([3, 5])) == [ [], [3], [3, 5], [5] ])
    assert(sorted(allSublists([6,7,8])) == [ [], [6], [6, 7], [6, 7, 8],
                                             [6, 8], [7], [7, 8], [8] ])
    print('Passed!')

def testSolveSubsetSum():
    def checkSubsetSum(L):
        solution = solveSubsetSum(L)
        for v in solution:
            assert(solution.count(v) <= L.count(v))
        assert(sum(solution) == 0)
    print('  Testing solveSubsetSum()...', end='')
    assert(solveSubsetSum([5,2,3,-4]) == None)
    checkSubsetSum([-1,5,2,3,-4])
    checkSubsetSum([8,19,31,27,52,-70,4])
    print('Passed!')

def testHeapsAlgorithmForPermutations():
    print('  Testing heapsAlgorithmForPermutations()...', end='')
    def f(): yield 42
    assert(type(heapsAlgorithmForPermutations([1])) == type(f())) # generator
    assert(sorted(heapsAlgorithmForPermutations([1])) == [[1]])
    assert(sorted(heapsAlgorithmForPermutations([1,2])) == [
            [1,2], [2,1]
        ])
    assert(sorted(heapsAlgorithmForPermutations([3,1,2])) == [
            [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
        ])
    print('Passed!')

def testSolveCryptarithmWithMaxDigit():
    print('  Testing solveCryptarithmWithMaxDigit()...', end='')
    assert(solveCryptarithmWithMaxDigit('RAM + RAT = ANT', 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert(solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 4) == None)
    assert(solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 5) == '''\
ANT + CAT = EEL
125 + 315 = 440''')
    print('Passed!')

def testGetAllSingletonCryptarithmsWithMaxDigit():
    print('  Testing getAllSingletonCryptarithmsWithMaxDigit()...', end='')
    words = ['EEL', 'RAM', 'CAT', 'BEE', 'FLY',
             'HEN', 'RAT', 'DOG', 'ANT']
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 3) == '')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '''\
ANT + CAT = EEL
125 + 315 = 440
ANT + CAT = HEN
105 + 315 = 420
ANT + RAT = EEL
125 + 315 = 440
ANT + RAT = HEN
105 + 315 = 420
BEE + EEL = FLY
411 + 112 = 523''')

    words = ['DEER', 'BEAR', 'GOAT', 'MULE', 'PUMA',
             'COLT', 'ORCA', 'IBEX', 'LION', 'WOLF']
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 6) == '''\
BEAR + DEER = IBEX
4203 + 1223 = 5426
COLT + GOAT = ORCA
4635 + 1605 = 6240''')
    print('Passed!')

def testSpicyCombinatoricsProblems():
    print('Testing spicy combinatorics problems...')
    testAllSublists()
    testSolveSubsetSum()
    testHeapsAlgorithmForPermutations()
    testSolveCryptarithmWithMaxDigit()
    testGetAllSingletonCryptarithmsWithMaxDigit()
    print('Passed!')

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # required
    testPersonClass()

    # # mild
    testDestructiveRemoveEvens()
    testNondestructiveRemoveEvens()

    # # medium
    # testBestScrabbleScore()
    testSolvesCryptarithm()
    # testDrawLetterTypePieChart()

    # # spicy
    # testSpicyCombinatoricsProblems()
    # testRunSimpleProgram()

def main():
    cs112_s20_unit4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
