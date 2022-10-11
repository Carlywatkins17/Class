# Carly Watkins
# 10/6
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# conditional exercises from night 1

# exercise 11

from multiprocessing import RLock


A = int(input("Enter a value for A: "))
B = int(input('Enter a value for B: '))
if B > 0:
    print("A + B is: " + str(A + B))
    print("A - B is: " + str(A - B))
    print("A * B is: " + str(A * B))
    print("A / B is: " + str(A / B))
    print("A % B is: " + str(A % B))
else:
    print('You can\'t divide by 0')
    print("A + B is: " + str(A + B))
    print("A - B is: " + str(A - B))
    print("A * B is: " + str(A * B))



# exercise 12

age = int(input('How old are you? '))
if age < 0:
    print('Invalid age')
if age <= 16: 
    print('You can\'t drive')
if age <= 18:
    print('You cant vote')
if age <= 21:
    print('You cant enjoy beer.')
if age >= 55:
    print('You get the senior discount')

#exercise 13

import random

Rock = 1 
Paper = 2 
Scissors = 3

User = int(input("Enter your choice: "))

Machine = (random.randrange(1,3))

print("The machine chooses " + str(Machine))

if User == 1 and Machine == 3:
    print('You win!')
if User == 1 and Machine == 2:
    print('The machine wins!')
if User == 2 and Machine == 1:
    print('You win!')
if User == 2 and Machine == 3:
    print('The machine wins!')
if User == 3 and Machine == 2: 
    print('You win!')
if User == 3 and Machine == 1:
    print('The machine wins!')
if User == Machine:
    print('Its a tie')




