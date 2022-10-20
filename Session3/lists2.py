# Carly Watkins
# 10/13
# CS-100A-x
# License: Copyright 2022 Carly Watkins
# Resources used: https://www.google.com/search?q=google+style+guide&rlz=1C1GCEJ_enUS1024US1024&oq=google+style&aqs=chrome.1.69i57j0i131i433i512j0i512l5j69i60.3639j1j7&sourceid=chrome&ie=UTF-8
#Exercises night 2

# Exercise 2
first = ['this' , 'is' , 'a' , 'list']
evens = [2,3,4]
students = ['Abby' , 'ben' ]

print(first)
print(evens + students)
    
   # create an empty list
team = []

# ask the user for names.
# enter 'done' when complete
player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

team.reverse()

print('your team is: ')
for p in team:
    print("\t" + p)
if 'Carly'in team:
    print('I can\'t wait to play!')
else:
    print('Put me in coach, I\'m ready to play!')
team.reverse()
