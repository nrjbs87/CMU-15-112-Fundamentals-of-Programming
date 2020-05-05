#################################################
# writing_session5_practice_solutions.py
#################################################

import cs112_s20_unit5_linter
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

def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    rows, cols = len(A), len(A[0]) 
    sol = make2dList(rows-1, cols-1)
    pushBack = False

    for row_index in range(rows):
        if (row_index != row):
            for col_index in range(cols):
                if (pushBack):
                    sol[row_index-1] = A[row_index][:col]
                    sol[row_index-1] += A[row_index][col+1:]
                else:
                    sol[row_index] = A[row_index][:col]
                    sol[row_index] += A[row_index][col+1:]
        else: 
            pushBack = True
    return sol

def destructiveRemoveRowAndCol(A, row, col):
    rows, cols = len(A), len(A[0])
    for row_index in range(rows):
        A[row_index].pop(col)
    A.pop(row)

def bestQuiz(a):
    rows = len(a)
    cols = len(a[0])
    quizTotal = []
    maxQuizTotal = 0
    highestScoringQuiz = -1

    for j in range(cols):
        quizTotal = []
        for i in range(rows):
            if( a[i][j] != -1):
                quizTotal += [ a[i][j] ]
            if quizTotal != [] and sum(quizTotal)/len(quizTotal) > maxQuizTotal:
                maxQuizTotal = sum(quizTotal)/len(quizTotal)
                highestScoringQuiz = j
    if highestScoringQuiz == -1: return None
    else: return highestScoringQuiz

def make2dList(rows, cols):
    return [ ([0] * cols) for row in range(rows) ]

def matrixAdd(L, M):
    Lrows, Lcols = len(L), len(L[0])
    Mrows, Mcols = len(M), len(M[0])

    if Lrows != Mrows or Lcols != Mcols:
        return None

    sol = make2dList(Lrows, Lcols)
    
    for row_index in range(Lrows):
        for col_index in range(Lcols):
            L_add = L[row_index][col_index]
            M_add = M[row_index][col_index]
            sol[row_index][col_index] = L_add + M_add
    return sol

def isMostlyMagicSquare(a):
    
    rows, cols = len(a), len(a[0])

    # check all rows are equal
    for rowIndex in range(rows):
        rowSum = sum(a[rowIndex])
        if rowIndex == 0: finalRowSum = rowSum
        elif rowSum != finalRowSum: return False

    # check all cols are equal
    for colIndex in range(cols):
        colList = []
        for rowIndex in range(rows):
            colList += [ a[rowIndex][colIndex]]
        colSum = sum(colList)
        if colIndex == 0: finalColSum = colSum
        elif colSum != finalColSum: return False

    # check all diagonals are equal
    diagList = []
    for rowIndex in range(rows):
        diagList.append(a[rowIndex][rowIndex])
    finalDiagSum = sum(diagList)

    negDiagList = []
    for rowIndex in range(rows):
        negDiagList.append(a[rowIndex][rows-1-rowIndex])
    finalNegDiagSum = sum(negDiagList)

    # check rowSum = colSum = diagSum = negDiagSum
    if (finalRowSum == finalColSum == finalDiagSum == finalNegDiagSum): 
        return True
    else: 
        return False

class DataTable(object):
    def __init__(self, csvString):
        # load the 2d list from the csv string
        self.rawData = csvString
        self.data = []
        for line in self.rawData.splitlines():
            self.data.append(line.strip().split(','))
        self.data.pop(0)
        self.data.pop(3)
         # and convert the strings to numbers (but skip the labels)
        rows, cols = len(self.data), len(self.data[0])
        for rowIdx in range(rows):
            for colIdx in range(cols):
                    if self.data[rowIdx][colIdx].isnumeric():
                        self.data[rowIdx][colIdx]=int(self.data[rowIdx][colIdx])

    def getDims(self):
        return (len(self.data), len(self.data[0]))

    def getColumn(self, columnIndex):
        return DataColumn(self.data, columnIndex)

class DataColumn(object):
    def __init__(self, dataTable, columnIndex):
        self.label = dataTable[0][columnIndex]
        data = []
        data += [dataTable[1][columnIndex]]
        data += [dataTable[2][columnIndex]]
        self.data = data

    def average(self):
        return int(sum(self.data)/2)

#################################################
# Test Functions
#################################################

def testNondestructiveRemoveRowAndCol():
    print('Testing removeRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    aCopy = copy.copy(a)
    assert(bestQuiz(a) == 2)
    assert(a == aCopy) # must be non-destructive!
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    assert(bestQuiz([[]]) == None)
    print('Passed')

def testMatrixAdd():
    print('Testing matrixAdd()...', end='')
    L = [ [1,  2,  3],
          [4,  5,  6] ]
    M = [ [21, 22, 23],
          [24, 25, 26]]
    N = [ [1+21, 2+22, 3+23],
          [4+24, 5+25, 6+26]]
    lCopy = copy.copy(L)
    mCopy = copy.copy(M)
    assert(matrixAdd(L, M) == N)
    assert((L == lCopy) and (M == mCopy)) # must be non-destructive!
    assert(matrixAdd(L, [ [ 1, 2, 3] ]) == None) # dimensions mismatch
    print('Passed!')

def testIsMostlyMagicSquare():
    print("Testing isMostlyMagicSquare()...", end="")
    assert(isMostlyMagicSquare([[42]]) == True)
    assert(isMostlyMagicSquare([[2, 7, 6],
                                [9, 5, 1],
                                [4, 3, 8]]) == True)
    assert(isMostlyMagicSquare([[4-7, 9-7, 2-7],
                                [3-7, 5-7, 7-7],
                                [8-7, 1-7, 6-7]]) == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMostlyMagicSquare(a))
    assert(isMostlyMagicSquare([[1, 2], [2, 1]]) == False) # bad diagonals!
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMostlyMagicSquare(a) == False) # it's close, but not quite!
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMostlyMagicSquare(a) == False) # ditto!
    print("Passed!")

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))

    column0 = dataTable.getColumn(0)
    assert(isinstance(column0, DataColumn))
    assert(column0.label == 'Name')
    assert(column0.data == ['Fred', 'Wilma'])

    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testMatrixAdd()
    testIsMostlyMagicSquare()
    testDataTableAndDataColumnClasses()

def main():
    cs112_s20_unit5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
