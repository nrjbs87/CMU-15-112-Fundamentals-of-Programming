#################################################
# hw7.py
#
# Your name: Raj Basu
# Your andrew id: neerajb
#################################################

import cs112_s20_unit7_linter
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
# Bird, Penguin, and MessengerBird classes
#################################################

# place your Bird, Penguin, and MessengerBird classes here

class Bird(object):

    isMigrating = False

    @staticmethod
    def startMigrating():
        Bird.isMigrating = True

    @staticmethod
    def stopMigrating():
        Bird.isMigrating = False

    def __init__(self, birdType):
        self.birdType = birdType
        self.eggs = 0
        
    def __eq__(self, other):
        return (self.birdType == other.birdType)

    def __repr__(self):
        typeBird = self.birdType
        numEggs = self.eggs
        if self.eggs == 1: return f'{typeBird} has {numEggs} egg'
        else: return f'{typeBird} has {numEggs} eggs'
    
    def layEgg(self):
        self.eggs+=1

    def countEggs(self):
        return self.eggs

    def fly(self):
        return "I can fly!"

class Penguin(Bird):

    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"

class MessengerBird(Bird):

    def __init__(self, birdType, secretMessage):
        super().__init__(birdType)
        self.secretMessage = secretMessage

    def deliverMessage(self):
        return self.secretMessage

#################################################
# Marble, ConstantMarble, and DarkeningMarble classes
#################################################

class Marble(object):

    marbleCounter = 0

    @staticmethod
    def getMarbleCount():
        return Marble.marbleCounter

    def __init__(self, colorString):
        Marble.marbleCounter += 1
        self.colorString = colorString.lower()
        self.colorStringL = self.colorString.split(',')
       
    def __eq__(self, other):
            if isinstance(self, Marble) and isinstance(other, Marble):
                return sorted(self.colorStringL) == sorted(other.colorStringL)
            else:
                return False

    def __repr__(self):
        self.colorString=str(sorted(self.colorStringL))
        self.colorString=self.colorString.strip('[]').replace("'", "")
        return f'<Marble with colors: {self.colorString}>'

    def colorCount(self):
        return len(self.colorStringL)

    def addColor(self, addColor):
        addColor = addColor.lower()
        if addColor not in self.colorStringL:
            self.colorStringL.append(addColor)
            return True
        else: return False

class ConstantMarble(Marble):

    def addColor(self, addColor):
        return False

class DarkeningMarble(Marble):

    def addColor(self, addColor):
        return super().addColor('dark' + addColor)
     

#########################################################
# NamedNumber spicy class
#########################################################

# Place your spicy NamedNumber class here (if you do this spicy problem)

#################################################
# Test Functions
#################################################
def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    tempBird = Bird("Parrot")
    assert(bird1 == tempBird)
    tempBird = Bird("Wren")
    assert(bird1 != tempBird)
    assert(getLocalMethods(Bird) == ['__eq__','__init__', 
                                     '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(not isinstance(bird1, Penguin))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that carries a message
    bird3 = MessengerBird("War Pigeon", "Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(not isinstance(bird2, MessengerBird))
    assert(not isinstance(bird1, MessengerBird))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon", "")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])

    # Note: all birds are migrating or not (together, as one)
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == False)
    assert(Bird.isMigrating == False)

    bird1.startMigrating()
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == True)
    assert(Bird.isMigrating == True)

    Bird.stopMigrating()
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == False)
    assert(Bird.isMigrating == False)
    print("Passed!")

def testMarbleClasses():
    print("Testing Marble classes...", end="")
    # A Marble takes a string (not a list) of comma-separated color names
    m1 = Marble('Pink,Cyan')
    assert(m1.colorCount() == 2) # pink and cyan
    assert(Marble.getMarbleCount() == 1) # we have created 1 marble so far

    # When converted to a string, the Marble includes the color names,
    # each separated by a comma and a space, and all lower-case, and listed
    # in alphabetical order:
    assert(str(m1) == '<Marble with colors: cyan, pink>')

    m2 = Marble('Red,Orange,yellow,GREEN')
    assert(str(m2) == '<Marble with colors: green, orange, red, yellow>')
    assert(m2.colorCount() == 4)
    assert(Marble.getMarbleCount() == 2) # we have created 2 marbles so far

    # This also works in a list:
    assert(str([m1]) == '[<Marble with colors: cyan, pink>]')

    # Equality works as expected:
    m3 = Marble('red,blue')
    m4 = Marble('BLUE,RED')
    m5 = Marble('red,green,blue')
    assert((m3 == m4) and (m3 != m5) and (m3 != "Don't crash here!"))
    assert(Marble.getMarbleCount() == 5) # we have created 5 marbles so far

    # You can add colors, which only change the marble if they are not present:
    assert(m3.addColor('Red') == False) # False means the color was not added,
                                        # because it was already there
    # and no changes here:
    assert(m3.colorCount() == 2)
    assert(str(m3) == '<Marble with colors: blue, red>')
    assert((m3 == m4) and (m3 != m5))

    # Once more, but with a new color:
    assert(m3.addColor('green') == True) # True means the color was added!
    # and so these all change:
    assert(m3.colorCount() == 3)
    assert(str(m3) == '<Marble with colors: blue, green, red>')
    assert((m3 != m4) and (m3 == m5))

    # A ConstantMarble is a marble that never changes its color:
    m6 = ConstantMarble('red,blue')
    assert(isinstance(m6, Marble))
    assert(str(m6) == '<Marble with colors: blue, red>')
    assert(m6.addColor('green') == False) # constant marbles never change!
    assert(str(m6) == '<Marble with colors: blue, red>')
    assert(Marble.getMarbleCount() == 6) # we have created 6 marbles so far
    assert(getLocalMethods(ConstantMarble) == ['addColor'])

    # A DarkeningMarble is a marble that prefixes 'dark' to any colors
    # that are added after it is first created.
    # Note: for full credit, you must use super() properly here!
    m7 = DarkeningMarble('red,blue')
    assert(isinstance(m7, Marble))
    assert(str(m7) == '<Marble with colors: blue, red>') # not darkened
    assert(m7.addColor('green') == True) # but green will become darkgreen
    assert(str(m7) == '<Marble with colors: blue, darkgreen, red>')
    assert(Marble.getMarbleCount() == 7) # we have created 7 marbles so far
    assert(getLocalMethods(DarkeningMarble) == ['addColor'])
    print("Passed!")

#########################################################
# NamedNumber class spicy test function
#########################################################

def testNamedNumberBasics():
    print('  testNamedNumberBasics()...', end='')

    # Note that NamedNumber.nameToNumber must be a static method
    # you are responsible for:
    # integers and floats between (-1000, +1000) exclusive (so no thousands)
    # floats may have only one digit after the decimal point
    # Just follow the examples below (though do not hardcode them, of course)
    # Names will not contain dashes, nor the word 'and', etc...
    # You do not have to handle all the strange variants
    # like 'negative negative five'
    assert(NamedNumber.nameToNumber('zero') == 0)
    assert(NamedNumber.nameToNumber('forty') == 40)
    assert(NamedNumber.nameToNumber('fifty') == 50)
    assert(NamedNumber.nameToNumber('negative thirty two') == -32)
    assert(NamedNumber.nameToNumber('three hundred eighteen point eight') ==
                                    318.8)
    assert(NamedNumber.nameToNumber('negative nine hundred point five') ==
                                    -900.5)
    assert(NamedNumber.nameToNumber('four hundred eighty') == 480)
    assert(NamedNumber.nameToNumber('four hundred eighty two') == 482)
    assert(NamedNumber.nameToNumber('four hundred eighty two point one') ==
                                    482.1)

    # Similarly, NamedNumber.numberToName must be a static method
    # that does the same thing in reverse:
    assert(NamedNumber.numberToName(0) == 'zero')
    assert(NamedNumber.numberToName(40) == 'forty')
    assert(NamedNumber.numberToName(50) == 'fifty')
    assert(NamedNumber.numberToName(-32) == 'negative thirty two')
    assert(NamedNumber.numberToName(318.8) ==
           'three hundred eighteen point eight')
    assert(NamedNumber.numberToName(-900.5) ==
           'negative nine hundred point five')
    assert(NamedNumber.numberToName(480) == 'four hundred eighty')
    assert(NamedNumber.numberToName(482) == 'four hundred eighty two')
    assert(NamedNumber.numberToName(482.1) ==
           'four hundred eighty two point one')

    # Now let's test __init__, __repr__, and __eq__:
    x = NamedNumber('forty')
    assert(str(x) == repr(x) == 'NamedNumber(forty)')
    assert((x.name == 'forty') and (x.number == 40))
    assert((x == 40) and (x == 40.0))
    assert(x == NamedNumber('forty'))
    assert(x == 'forty') # this may be unexpected!
    assert(x != 50)
    assert(x != NamedNumber('fifty'))
    assert(x != 'do not crash here!')

    # We can create a named number using either the number or the name: 
    assert(NamedNumber(-42) == NamedNumber('negative forty two'))
    assert(NamedNumber(200.1)) == NamedNumber('two hundred point one')

    print('Passed!')

def testNumericMethods():
    # Tests __float__, __add__, __radd__
    # (Naturally, similiar methods exist for -, *, /, //, **, %, ...)
    print('  testNumericMethods()...', end='')
    assert(float(NamedNumber('forty point three')) == 40.3)
    x = NamedNumber('forty')
    assert((x + 1) == NamedNumber('forty one')) # this uses __add__
    assert((2 + x) == NamedNumber('forty two')) # this uses __radd__
    assert((NamedNumber('point one') + x) == NamedNumber(40.1))
    assert(x == 40)
    x += 42
    assert(x == NamedNumber('eighty two'))

    # You should be able to figure out what other methods this requires
    # so that it can multiply to and subtract from NamedNumber instances...
    assert(NamedNumber(42)*10 - NamedNumber(20) == 400)
    print('Passed!')

def testRichComparisonMethods():
    # Tests __lt__, __le__, __gt__, and __ge__
    print('  testRichComparisonMethods()...', end='')
    assert(NamedNumber(5.3) < NamedNumber(5.4))
    assert(NamedNumber(5.3) <= 5.4)
    assert(NamedNumber(5.4) > NamedNumber(5.3))
    assert(5.4 >= NamedNumber(5.3))
    print('Passed!')

def testCallableObjects():
    # Tests __call__
    print('  testCallableObjects()...', end='')
    # This lets us *call* the object as though it were a function!
    # Here, the function will take a non-negative int n (don't worry about
    # other cases) and return a list containing n copies of this NamedNumber,
    # like so: 
    x = NamedNumber(42)
    assert(x(3) == [NamedNumber(42), NamedNumber(42), NamedNumber(42)])
    assert(x(0) == [])
    y = NamedNumber(-112)    
    assert(y(1) == ["negative one hundred twelve"])
    assert(y(3) == ["negative one hundred twelve", -112, NamedNumber(-112)])
    print('Passed!')

def testNamedNumberClass():
    print('Testing NamedNumber Class...')
    testNamedNumberBasics()
    testNumericMethods()
    testRichComparisonMethods()
    testCallableObjects()
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # required
    # testShortAnswers()

    # mild + medium
    testBirdClasses()
    testMarbleClasses()

    # spicy
    # testNamedNumberClass()

def main():
    cs112_s20_unit7_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
