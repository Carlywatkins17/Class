#Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
#Exercises night 2

# Exercise 3
# Write a program that asks the user for items for a grocery list. Then, as the user is walking through the store, they can input what they just put in their cart. 
# If that item is in the list, remove that item (using remove). And if the list is empty, tell the user they can check out now. Here's an example execution:

from operator import truediv


cart = []


item = ''
while item != 'done':
    item = input('enter a grocery item, price, and quantity, or done to exit: ')
    if item != 'done':
        cart.append(item)
    else:
        print(cart)
        print('Time to shop!')


while cart != False:
    x = input('Check off an item: ')
    if x in cart:
        cart.remove(x)
        print(cart)
        if not cart:
            print("Time to check out.")
            break
    else:
        print('That is not in the cart')
        print(cart)
        # x = input('Check off an item: ')

#while cart == False:
#    print ('Time to check out.')








