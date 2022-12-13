from createbeds import bed 
from beduserinput import beds 
import json
from savebedstofile import save_beds

#calculates the size of the bed 
#I need to know how to call upon an entity from the txt file. For now I am just calling on "the bed.  I also want to be able to call on more than one at a time like, "Which beds do you need the sizes of?


def dimension():
    for s in beds: 
        print(s.name + " is " + str(int(s.length)*int(s.width)) + " sq ft" ) 


                    
#this is bad it goes forever
#sizes = []
#def dimension():
    #for d in beds:
       #d.name = input('Which bed do you need the size of?: ')
       #print(d.name + " is " + str(int(d.length)*int(d.width)) + " sq ft" )

            

# solicits user input on which beds need more soil and calculates the volume needed in units that the product is sold in.
# same problem with bed vs beds.  If I refer to the class "For s in bed" I get an error that 'type' object is not iterable. 
#if I refer to the list beds "For s in beds" I can at least get output but only based on the last thing I did in that list (which can be found on beduserinput.py)
def soil():
    for s in beds:
        print('You need ' + str((int(s.length) * int(s.width) * int(s.depth))/27) + " cubic yards of soil")

