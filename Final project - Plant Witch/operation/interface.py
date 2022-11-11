from datetime import date, timedelta, datetime
from createbeds import getuserresponse, save_beds, fertilize_calendar, dimension, nfd, soil
from createplants import getuserresponse, save_plants

print('Welcome to Plant-Witch 2023!')
user = input('What is your name?: ')
garden = input('What is your garden name?: ')
print('Thank you ' + user + '.' + 'Let\'s start your garden!')

save_beds()


calendar = input('Would you like a fertilization schedule? yes or no: ') 
if calendar == 'yes':
    fertilize_calendar()

sched = input('Are you on schedule for fertilizing? yes or no:')
if sched == 'no':
    bd = input('which bed do you need the next fertilize date for?: ')
    nfd(bd.bed)

dirt = input('Do you need bed dimensions? yes or no: ')
if dirt == 'yes':
    dimension()

order = input('Do you need to calculate the your soil order size? yes or no: ')
if order == 'yes':
    soil()

save_plants()
