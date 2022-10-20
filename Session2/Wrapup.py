# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
#Exercises night 2


username = input('What is your name? ')

import random

A = (random.randrange(1,100))
B = (random.randrange(1,100))
C = (random.randrange(1,100))
D = (random.randrange(1,100))
E = (random.randrange(1,100))
F = (random.randrange(1,100))

def getuserresponse(x,y,op):
    ans = int(input('What is ' + str(x) + ' ' + op + ' ' + str(y) + '?: '))
    return ans 
#convert variables to lower case

def testuser(x,y,op,question,answer):
    if getuserresponse(x,y,op) == answer:
        print(question + ': correct')

    else:
        print(question +  ' incorrect. The correct answer is ' + str(answer))

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))
print("D = " + str(E))
print("E = " + str(F))

testuser(A,B,'+','question 1', A + B)
testuser(A,B,'-','question 2', A - B)
testuser(A,B,'*', 'question 3', A * B)
testuser(A * B,B,'/', 'question 4',A)
testuser(A,B,'%', 'question 5', A % B)
