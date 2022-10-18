# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# exercises from night 2

#Exercise 4 go back to rock paper scissors.  make it loop until someone wins 

from platform import machine
import random

Rock = 1 
Paper = 2 
Scissors = 3

print ("Rock is 1, Paper is 2, Scissors is 3")

User = int(input("Enter your choice: "))

Machine = (random.randrange(1,3))

print("The machine chooses " + str(Machine))

if User == 1 and Machine == 3:
    print('You win!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == 1 and Machine == 2:
    print('The machine wins!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == 2 and Machine == 1:
    print('You win!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == 2 and Machine == 3:
    print('The machine wins!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == 3 and Machine == 2: 
    print('You win!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == 3 and Machine == 1:
    print('The machine wins!')
    User = int(input("Enter your choice: "))

    Machine = (random.randrange(1,3))

    print ("Rock is 1, Paper is 2, Scissors is 3")

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
        print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))

if User == Machine:
    print('Its a tie.  Pick again')
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
        print('Its a tie.  Pick again')
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
            print('Its a tie.  Pick again')
        User = int(input("Enter your choice: "))