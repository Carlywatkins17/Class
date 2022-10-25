#Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8


# Exercise 5 Modify that program further by printing out a receipt once the cart is empty. Also print out the total cost of the items in the cart.

cart = []

item = ""
while item != 'done':
    item = input('enter a grocery item, or done to exit: ')
    if item != 'done':
        cart.append(item)
    else:
        print(cart)
        print('Time to shop!')

receipt = []

while cart != False:
    x = input('Check off an item: ')
    if x in cart:
        cart.remove(x)
        price = float(input('What is the price?: '))
        qty = int(input('How many?: '))
        receipt.append((x, price, qty))
        print(cart)
        if not cart:
            print("Time to check out.")
            for item in receipt:
                (thing, price, qty) = item
                print(str(qty) + ' X ' + thing + ' : $ ' + str(qty*price))
            break
    else:
        print('That is not in the cart')
        price = float(input('What is the price?: '))
        qty = int(input('How many?: '))
        receipt.append((x, price, qty))
        # x = input('Check off an item: ')

#while cart == False:
#    print ('Time to check out.')