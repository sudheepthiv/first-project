import os
from collections import namedtuple
from collections import Counter

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

fruits = ('apple', 'gauva', 'orange')

# Declaring namedtuple() 
fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
apple = fruit(number=5,variety='Granny Smith',color='red')

print(__name__)
