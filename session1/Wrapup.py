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
Q2 = int(input("What is A - B ? "))
Q3 = int(input("What is C * D ? "))
Q4 = int(input("What is E / F ? "))


if Q1 == A + B:
    print('Queston 1: correct')
elif Q1 != A + B:
    print('Question 1 incorrect. The correct answer is ' + str(A + B))

if Q2 == A - B:
    print('Queston 2: correct')
elif Q2 != A - B:
    print('Question 2 incorrect. The correct answer is ' + str(A - B))

if Q3 == C * D:
    print('Queston 3: correct')
elif Q3 != C * D:
    print('Question 3 incorrect. The correct answer is ' + str(C * D))

if Q4 == E / F:
    print('Queston 4: correct')
elif Q4 != E / F:
    print('Question 4 incorrect. The correct answer is ' + str(E / F))


