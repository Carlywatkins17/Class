#Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
#Exercises night 2

# Exercise 3
# Write a program that asks the user for items for a grocery list. Then, as the user is walking through the store, they can input what they just put in their cart. 
# If that item is in the list, remove that item (using remove). And if the list is empty, tell the user they can check out now. Here's an example execution:

cart = []

def makelist():
    item = ''
    while item != 'done':
        item = input('enter a grocery item, or done to exit: ')
        if item != 'done':
            cart.append(item)
        else:
            print('Time to shop!')
makelist()
print(cart)

def clearlist():
    x = input('Check off an item: ')
    for x in cart:
        cart.remove(x)
        print(cart)
        if x not in cart: 
            print('That was not in the cart.')
        else:
            print('You can check out now.')