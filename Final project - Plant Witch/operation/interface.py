from datetime import date, timedelta, datetime
from createbeds import getuserresponse, save_beds, fertilize_calendar, dimension, nfd, soil
from createplants import getuserresponse, save_plants

print('Welcome to Plant-Witch 2023!')
user = input('What is your name?: ')
garden = input('What is your garden name?: ')
print('Thank you ' + user + '.' + 'Let\'s start your garden!')

save_beds()


calendar = input('Would you like a fertilization schedule? yes or no: ') 
if calendar != 'no':
    fertilize_calendar()
    input('Would you like a fertilization schedule? yes or no: ') 

sched = input('Are you on schedule for fertilizing? yes or no:')
if sched != 'yes':
    nfd()

dirt = input('Do you need bed size? yes or no: ')
if dirt != 'no':
    dimension()
    input('Do you need bed size? yes or no: ')

save_order = []
order = input('Do you need to calculate your soil order volume? yes or no: ')
if order != 'no':
    soil()

# I want to allow the user to sum the volume of several beds for the soil order. 

save_plants()
