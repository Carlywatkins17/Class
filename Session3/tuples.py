#Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8


# Exercise 4 Modify your grocery list program from earlier to take the item, the price, and the quantity when the user picks up each item and puts it in the cart.

cart = []


item = ("item", "price in dollars", "quantity")
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
