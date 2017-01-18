'''
Created on 05 gen 2017
Esempi di Python
@author: radin
'''

# somme
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y+a

print(add(1,2))
print(addFixedValue(1))

# nome
name = input('What is your name?\n')
print('Hi, %s.' % name)

# ciclo for
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
    
# Fibonacci
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
    
# somma interi
import sys


try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')