from datetime import date, timedelta, datetime
from createbeds import bed
from createplants import plants, herbs, vegetables, flowers
from saveplantstofile import save_plants
from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
from beduserinput import getuserresponse,  beds
from size import dimension, soil
from savebedstofile import save_beds
from fertilization import fert_cal, nfd
import json


print('Welcome to Plant-Witch 2023!')
user = input('What is your name?: ')
garden = input('What is your garden name?: ')
print('Thank you ' + user + '.' + ' Let\'s start your garden!')

save_beds()

sched = input('Are you on schedule for fertilizing? yes or no:')
if sched == 'no':
    nfd()
else:
    fert_cal()


dirt = input('Do you need the bed size? yes or no: ')
if dirt != 'no':
    dimension()


save_order = []
order = input('Do you need to calculate your soil order volume? yes or no: ')
if order != 'no':
    soil()

# I want to allow the user to sum the volume of several beds for the soil order. 

f = open('../data/plants.txt', 'r')
plant_data=json.loads(f.read())
f.close()
for p in plant_data['plant']:

    plant_names[p['name']]=plants(p['name'], p['quantity'],p['sun'], p['drainage'] ,p['water'], p[bed], p['seasonality'], p['storage'], p['fert'], p['sow_time'], p['sow_loc'], p['sow_depth'], p['sow_space'], p['height'], p['germ_time'], p['notes'] )
    
for h in plant_data['herb']:
    herb_deets[p['name']]=herbs(h['name'], h['smoke'], h['burn'], h['edible'])
    
for v in plant_data['vegetable']:
    veg_deets[p['name']]=vegetables(v['name'], v['reap'])

for fl in plant_data['flower']:
    flower_deets[p['name']]=flowers(fl['name'], fl['color'], fl['safety'], fl['smoke'], fl['burn'], fl['edible'])

#for h in plant_data['herb']

save_plants()

