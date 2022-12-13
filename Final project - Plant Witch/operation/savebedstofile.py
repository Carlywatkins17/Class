from createbeds import bed 
from datetime import date, timedelta, datetime
import _strptime
from beduserinput import beds, getuserresponse
import json

# writes the user input/class data to a file        
def save_beds():
    f = open('../data/the_beds_list.txt', 'w')
    f.write(' \n')
    getuserresponse() 
    bed_data={}
    bed_json=[]

    for key in beds:
        b=beds[key]
        bed_json.append(b.toJSON())
        # f.write(b.name ) 
        # f.write(b.length, )
        # f.write(b.width, )
        # f.write(b.depth, )
        # f.write(b.sun, )
        # f.write(b.drainage, )
        # f.write(str(b.ffd),  )
        # f.write(str(b.pfd),  )
        # f.write(str(b.finfd), )
    bed_data['bed']=bed_json

    f.write(json.dumps(bed_data))
