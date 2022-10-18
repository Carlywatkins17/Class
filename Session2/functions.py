# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# exercises from night 2

#Exercise 6 Take the code that sums from 1 to a number and convert it into a function.  Also, make a similar function that calculates the factorial for a number (1*2*3*$...*n).

from re import X


def sum():
    n = int(input('enter a number: '))
    sum = 0
    for x in range (1, n):
        sum = sum + x
    print('The sum from 1 to ' + str(n) + ' is ' + str(sum))


def factorial():
    n = int(input('enter a number: '))
    product = 1
    for x in range (1, n):
        product *= product * n 
    print ('The factorial product from 1 to ' + str(n) + ' is ' + str(product))

sum()
factorial()






