username = input('What is your name? ')

import random

A = (random.randrange(1,100))
B = (random.randrange(1,100))
C = (random.randrange(1,100))
D = (random.randrange(1,100))
E = (random.randrange(1,100))
F = (random.randrange(1,100))
print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))
print("D = " + str(E))
print("E = " + str(F))


Q1 = int(input("What is A + B ? "))
if Q1 == A + B:
    print('Thats right!')
elif Q1 != A + B:
    print('The correct answer is ' + str(A + B))



