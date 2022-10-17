# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
# exercises from night 2

# Strings Exercises

#Exercise 1 Write a program that asks the user for a string and then outputs that string in various forms: upper case, lower case, and "title case".

from base64 import encode
from gettext import find
from itertools import count
from operator import index
from tkinter import CENTER


text = (input('Give me a string: '))
print(text.upper())
print(text.lower())
print(text.istitle())

#Exercise 2 Write program asks the user for alink to a website.  Use the startswith to check that the link starts with the string http.  
# If it does, thank the user for giving a valid link
#If not, tell the user they gave an invalid link.  

Thanks = True
link = input('Please enter the URL of your favorite weather website: ')
if link.startswith('http') == True:
    print('Thank you')
elif link.startswith('http') == False:
    print('That is an invalid link')

    
#Exercise 3 One of the important functions for strings is strip, which removes spaces at the beginning and the end of the string. 
# That is, if I have text = ' hello ', newtext = text.strip() will result with the value 'hello' in newtext. 
# Write a program that asks the user for their name, then outputs a welcome text to the the user with their name, 
# using strip() to make sure the name doesn't have spaces surrounding it.

name = (input('What is your name? '))
newname = (name.strip())

print('Welcome to class ' + newname)





















