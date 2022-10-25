#Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8


# Exercise Modify your tutor program to add each equation to a list so you can keep a record of all the equations.
# Now modify that again to keep each equations in a tuple. Store the equation, the correct answer, and the user's answer.
# when the equations are complete, go through your list and output the equation, the user's answer, and whether they got that correct so they can review the equations.
# Test your program carefully. Then commit and push your tutoring system to github. We will be building on this for the next 3 weeks.

import random

#create an empty list
qlist = []

#ask the computer to randomly generate a whole whole number for each variable
A = (random.randrange(1,100))
B = (random.randrange(1,100))
C = (random.randrange(1,100))
D = (random.randrange(1,100))
E = (random.randrange(1,100))
F = (random.randrange(1,100))

#This function asks an arithmetic question using the random variables above,
# returns the answer 

def getuserresponse(x,y,op):
    q = 'What is ' + str(x) + ' ' + op + ' ' + str(y) + '?: '
    qlist.append(q)
    ans = int(input(q))
    return ans


# this function tests the user
# it says if the answer is correct, tell the user as much,
# if it is not, tell them so, and the correct answer

def testuser(x,y,op,question,answer):
    if getuserresponse(x,y,op) == answer:
        print(question + ': correct')

    else:
        print(question +  ' incorrect. The correct answer is ' + str(answer))

#this set of print statements prints the random variables

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))
print("D = " + str(E))
print("E = " + str(F))

#this is a call for the previously defined function 'testuser' 
# which itself calls 'getuser response'
# thus asking the user the question, and responding to the validity of the answer.

testuser(A,B,'+','question 1', A + B)
testuser(A,B,'-','question 2', A - B)
testuser(A,B,'*', 'question 3', A * B)
testuser(A * B,B,'/', 'question 4',A)
testuser(A,B,'%', 'question 5', A % B)

print(qlist)




