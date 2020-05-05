#################################################
# writing_session4_practice_solutions.py
#################################################

import cs112_s20_unit4_linter
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

def alternatingSum(L):
    sol = 0
    multi = 1
    if len(L) == 0: return 0
    else:
        for item in L:
            sol += (item * multi)
            multi *= -1
    return sol

def median(L):
    if len(L) == 0: return None
    else:
        copyL = sorted(copy.copy(L))
        mid_index = len(copyL)//2
        if len(copyL) % 2 != 0:sol = copyL[mid_index]
        else:sol = (copyL[mid_index] + copyL[mid_index - 1]) / 2
    return sol

def isSorted(L):
    if len(L) == 0: return True
    minL = min(L)
    maxL = max(L)
    if L[0] == minL: # assume the listed in sorted smallest -> largest
        for item in L:
            if item >= minL: minL = item
            else: return False
        return True
    else: # assume the listed in sorted largest -> smallest 
        for item in L:
            if item <= maxL: maxL = item
            else: return False
        return True 

def smallestDifference(L):
    if len(L) == 0: return -1
    else:
        L = sorted(L)
        smallest_dif = 1000000
        for index in range(len(L)-1):
            dif = abs(L[index] - L[index+1])
            if(dif < smallest_dif):
                smallest_dif = dif
        return smallest_dif

def lookAndSay(L):
    if L == []: return L
    sol = []
    unique_item = L[0] # random float to compare with
    count = 1
    for i in range(1, len(L)):
        if L[i] == unique_item:
            count +=1
        else:
            sol.append((count, unique_item))
            count = 1
            unique_item = L[i]
    sol.append((count, unique_item))
    return sol

def inverseLookAndSay(L):
    sol = []
    for item in L:
        count, number = item[0], item[1]
        sol += [number]* count
    return sol

def nondestructiveRemoveRepeats(L):
    sol = []
    for item in L:
        if item not in sol:
            sol.append(item)
    return sol

def destructiveRemoveRepeats(L):
    unique_list = []
    for item in L:
        if item not in unique_list:
            unique_list.append(item)

    for i in range(len(unique_list)):
        while(L.count(L[i]) > 1):
            index = L.index(L[i], i+1)
            L.pop(index)

class VoteTally(object):

    def __init__(self, namelist):
        self.candidates = namelist
        self.votes = [0] * len(namelist)

    def addVotes(self, num_votes, name):
        if name not in self.candidates: 
            return 'No such candidate as ' + name
        else:
            index = self.candidates.index(name)
            self.votes[index] += num_votes

    def getVotes(self, name):
        if (name == 'Total'):
            return sum(self.votes)
        elif(name not in self.candidates):
            return 'No such candidate as ' + name
        else:
            index = self.candidates.index(name)
            return self.votes[index]
    
    def addVoteTally(self, new_vt):
        old_candidates = self.candidates[:]
        old_votes = self.votes[:]
        new_candidates = new_vt.candidates[:]
        new_votes = new_vt.votes[:]
        for i in range(len(new_candidates)):
           if old_candidates[i] in new_candidates:
               pop = new_candidates.index(old_candidates[i])
               old_votes[i] = old_votes[i] + new_votes[pop]
               new_candidates.pop(pop)
               new_votes.pop(pop)
        old_candidates += new_candidates
        old_votes += new_votes
        vt = VoteTally(old_candidates)
        vt.votes = old_votes
        return vt

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed.')

def testMedian():
    print('Testing median()...', end='')
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed')

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

def testVoteTallyClass():
    print('Testing VoteTally class...', end='')

    # When we create a VoteTally, we provide a list of
    # candidates whose votes we are tallying:
    vt1 = VoteTally(['Fred', 'Wilma', 'Betty'])

    # We can then add votes for the candidates
    vt1.addVotes(5, 'Fred')
    vt1.addVotes(3, 'Wilma')
    vt1.addVotes(2, 'Fred')

    # If we add votes to a non-candidate, we do so gracefully:
    assert(vt1.addVotes(3, 'Bam-Bam') == 'No such candidate as Bam-Bam')

    # And we can get the total tally of votes for each candidate
    assert(vt1.getVotes('Fred') == 7)
    assert(vt1.getVotes('Wilma') == 3)
    assert(vt1.getVotes('Betty') == 0)

    # And we can gracefully handle non-candidates
    assert(vt1.getVotes('Barney') == 'No such candidate as Barney')

    # And we can also get the overall total
    assert(vt1.getVotes('Total') == 10)

    # Here is a second VoteTally with some (but not all) of the same candidates
    vt2 = VoteTally(['Fred', 'Barney', 'Betty']) 
    vt2.addVotes(5, 'Fred')
    vt2.addVotes(2, 'Betty')
    vt2.addVotes(8, 'Betty')
    assert(vt2.getVotes('Fred') == 5)
    assert(vt2.getVotes('Wilma') == 'No such candidate as Wilma')
    assert(vt2.getVotes('Betty') == 10)
    assert(vt2.getVotes('Barney') == 0)
    assert(vt2.getVotes('Total') == 15)

    # We can combine two VoteTally objects to create a third
    # VoteTally object, which includes all the candidates from either
    # tally, and combines their totals:
    vt3 = vt1.addVoteTally(vt2)
    assert(vt1.candidates == ['Fred', 'Wilma', 'Betty']) # unchanged
    assert(vt2.candidates == ['Fred', 'Barney', 'Betty']) # ditto
    # but the new VoteTally is created with a sorted list of candidates
    # in the same order as they appear first in vt1 then vt2,
    # but with no duplicates
    assert(vt3.candidates == ['Fred', 'Wilma', 'Betty', 'Barney'])
    assert(vt3.getVotes('Fred') == 12)
    assert(vt3.getVotes('Wilma') == 3)
    assert(vt3.getVotes('Betty') == 10)
    assert(vt3.getVotes('Barney') == 0)
    assert(vt3.getVotes('Pebbles') == 'No such candidate as Pebbles')
    assert(vt3.getVotes('Total') == 25)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()
    testMedian()
    testIsSorted()
    testSmallestDifference()
    testLookAndSay()
    testInverseLookAndSay()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testVoteTallyClass()

def main():
    cs112_s20_unit4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
