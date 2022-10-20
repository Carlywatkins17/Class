# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# exercises from night 2

#Exercise 6 Take the code that sums from 1 to a number and convert it into a function.  Also, make a similar function that calculates the factorial for a number (1*2*3*$...*n).


from ast import Num, While
from calendar import month
from distutils.archive_util import make_archive
from random import randrange
from stat import FILE_ATTRIBUTE_TEMPORARY


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
        product = product * x 
    print ('The factorial product from 1 to ' + str(n) + ' is ' + str(product))
    
sum()
factorial()


# Exercise 7 Write a function that takes a string and adds up all the digits in that input.  For example, if the user enters "Whitworth 91" - George Fox 67", 
# I'd expect the function to return 23 (9+1+6+7). Test that function by getting an input from the user and outputting that sum.

def sumnum(text):
    number = 0
    for x in text:
        if x.isdigit() == True:
            Q = int(x)
            number = number + int(Q)

    return number

text = input('Please enter the name of each item and its count in inventory: ')
ttl = sumnum(text)
print('The total number of inventory items is: ' + (str(ttl)))


# Exercise 8 Write a function that takes a number between 1 and 12 and returns the month associated with that number (e.g. getmonth(1) would return "January" 
# and getmonth(9) would return "September".


def getmonth(month):

    if month == '1':
        print('Jan')
    if month == '2': 
        print('Feb')
    if month == '3':
        print('Mar')
    if month == '4': 
        print('Apr')
    if month == '5':
        print('May')        
    if month == '6': 
        print('Jun')
    if month == '7':
        print('Jul')
    if month == '8': 
        print('Aug')
    if month == '9': 
        print('Sep')
    if month == '10': 
        print('Oct')
    if month == '11': 
        print('Nov')
    if month == '12': 
        print('Dec')

month = input('Please enter a number from 1-12 to call month: ')
    
while month.isdigit() == False or int(month) < 1 or int(month) > 12:
        print('that is not a valid selection please try again')
        month = int(input('Please enter a number from 1-12 to call month: '))

getmonth(month)





