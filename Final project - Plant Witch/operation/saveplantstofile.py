from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
from createplants import plants, herbs, vegetables, flowers
import json
  
# writes the user input/class data to a file        
def save_plants():
    f = open('../data/plants.txt', 'w')
    f.write(' \n')
    getuserresponse() 
    plant_data={}
    plant_json=[]
    herb_json=[]
    vegetable_json=[]
    flower_json=[]
    
    for key in plant_names:
        p=plant_names[key]
        plant_json.append(p.toJSON())
        # f.write(p.name) #repeat for other properties
        # f.write(p.quantity)
        # f.write(p.sun)
        # f.write(p.drainage)
        # f.write(p.water)
        # f.write(p.bed)
        # f.write(p.seasonality)
        # f.write(p.storage)
        # f.write(p.fert)
        # f.write(p.sow_time)
        # f.write(p.sow_loc)
        # f.write(p.sow_depth)
        # f.write(p.sow_space)
        # f.write(p.height)
        # f.write(p.germ_time)
        # f.write(p.notes)

        #cntl/ comment all highlights
    #f.write(json.dumps(plant_json))
    plant_data['plant']=plant_json

    for key in herb_deets:
        h=herb_deets[key]
        # f.write(h.smoke)
        # f.write(h.burn)
        # f.write(h.edible)
        herb_json.append(h.toJSON())

    #f.write(json.dumps(herb_json))
    plant_data['herb']=herb_json
       
    for key in veg_deets:
        v=veg_deets[key]
        # f.write(v.reap)
        vegetable_json.append(v.toJSON())
    
    #f.write(json.dumps(vegetable_json))
    plant_data['vegetable']=vegetable_json

    for key in flower_deets:
        fl=flower_deets[key]
        # f.write(fl.color)
        # f.write(fl.safety)
        # f.write(fl.smoke)
        # f.write(fl.burn)
        # f.write(fl.edible)
        flower_json.append(fl.toJSON())

    #f.write(json.dumps(flower_json))
    plant_data['flower']=flower_json

    f.write(json.dumps(plant_data))

