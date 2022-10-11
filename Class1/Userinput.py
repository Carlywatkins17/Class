# Carly Watkins
# 10/6
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# Variable exercises from night 1

A = int(input("Choose a an interger to represent A: "))
B = int(input("Enter an interger for B: "))
C = int(input("Enter an interger number for C: "))

D = float(input("Choose a real number for D: "))
E = float(input("Choose a real number for E: "))
F = float(input("Choose a real number for F: "))

Q1 = int(input("What is A + B? "))
if Q1 == (A + B):
    print("Thats right!")
elif Q1 != (A + B):
    print("The correct answer is " + str(A + B))
    

Q2 = int(input("What is B - C? "))
if Q2 == (B - C):
    print("Thats right!")
elif Q2 != (B - C):
    print("The correct answer is " + str(B - C))
    

Q3 = int(input("What is C * D? "))
if Q3 == (C * D):
    print("Thats right!")
elif Q3 != (C * D):
    print("The correct answer is " + str(C * D))
    

Q4 = float(input("What is D / E? "))
if Q4 == (D / E):
    print("Thats right!")
elif Q4 != (D / E):
    print("The correct answer is " + str(D / E))
    

Q5 = float(input("What is the remainder of E / F? "))
if Q5 == (E % F):
    print("Thats right!")
elif Q5 != (E % F):
    print("The correct answer is " + str(E % F))
    
# Exercise 5, see variable.py

# Exercise 6 

game1 = int(input("What was the score for game 1? "))
game2 = int(input("What was the score for game 2? "))
game3 = int(input("What was the score for game 3? "))
game4 = int(input("What was the score for game 4? "))
game5 = int(input("What was the score for game 5? "))

print("The average score was " + str((game1 + game2 + game3 + game4 + game5)/5))


# exercise 7

bill = int(input("How much is the bill? "))
people = int(input("How many people will split it? "))
print("Your portion is " + str(bill + people) + "dollars.")

















