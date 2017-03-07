#see http://cs231n.github.io/python-numpy-tutorial/#python-basic

#Numbers
x = 3
print type(x)
print x, x + 1 ,x * 2, x ** 2
x+=1
print x
y = 2.5
print type(y)
print y, y + 1, y * 2, y ** 2

#Booleans
t = True
f = False
print type(t)
print t and f
print t or f
print not t
print t != f

#Strings
hello = 'hello'
world = 'world'
print hello
print len(hello)
hw = hello + ' ' + world
print hw
hw12 = '%s %s %d' % ( hello, world, 12)
print hw12

s = "hello"
print s.capitalize()
print s.upper()
print s.rjust(7)
print s.center(7)
print s.replace('l', '(ell)')
print ' world '.strip()

#Lists
xs = [3, 1, 2]
print xs, xs[2]
print xs[-1]
xs[2] = 'foo'
print xs
xs.append('bar')
print xs
x = xs.pop()
print x, xs

#Slicing
nums = range(5)
print nums
print nums[2:4]
print nums[2:]
print nums[:2]
print nums[:]
print nums[:-1]
nums[2:4] = [8, 9]
print nums

#Loops
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

#List comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares
#or
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares

#Dictionaries
d = {'cat': 'cute', 'dog': 'furry'}
print d['cat']
print 'cat' in d
d['fish'] = 'wet'
print d['fish']
print d.get('monkey', 'N/A')
print d.get('fish', 'N/A')
del d['fish']
print d.get('fish', 'N/A')

#Loops
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)

animals = {'cat', 'dog'}
print 'cat' in animals
print 'fish' in animals
animals.add('fish')
print 'fish' in animals
print len(animals)
animals.add('cat')
print len(animals)
animals.remove('cat')
print len(animals)

#Loops-sets
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

#Set comprehensions
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums

#Tuples
d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print type(t)
print d[t]
print d[(1, 2)]

#Functions
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print sign(x)

def hello(name, loud=False):
    if loud:
        print 'HELLO, %s!' % name.upper()
    else:
        print 'Hello, %s' % name

hello('Bob') # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"

#Classes
class Greeter(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
        
    # Instance method
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name
        
g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
