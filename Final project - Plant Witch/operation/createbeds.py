# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, edited June 9 2021, accessed October 31 2022

from datetime import date, timedelta, datetime


class bed:
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='01/01/1999', pfd='01/01/1999', finfd='01/01/1999'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = datetime.strptime(ffd, '%m/%d/%Y')  
        self.pfd = datetime.strptime(pfd, '%m/%d/%Y') 
        self.finfd = datetime.strptime(finfd, '%m/%d/%Y') 


    
#referenced stack overflow user Burnash "Iterating through a range of dates in python" edited code to my specifications.
# from datetime import date, timedelta
#start_date = date(2019, 1, 1)
#end_date = date(2020, 1, 1)
#delta = timedelta(days=1)
#while start_date <= end_date:
#    print(start_date.strftime("%Y-%m-%d"))
#    start_date += delta

#creates a calendar of that years recommended fertilization dates for that bed

    save_cal = []
    def fertilize_calendar(self):
        delta = timedelta(weeks=2)
        c = input('Which bed would you like the calendar for?: ')
        for c in bed:
            if self.ffd <= self.finfd:
                print(self.ffd)
                self.ffd += delta
                

 # calculates the next fertilization date based on last date and recommended frequency 

                         
    def nfd(self):
        delta = timedelta(weeks=2)
        b = input('What bed do you need the next fertilization date for? Type name or done: ')
        for b in bed:
            while self.pfd <= self.finfd: 
                text=input("The next fertilize date is: " + str(self.pfd + delta))
                return text
            
            
   #calculates the size of the bed 
    
    def dimension(self):
        for d in bed:
            d = input('Which bed do you need the size of?: ')
            print(d + " is " + str(self.length*self.width) + " sq ft" )
            

    # solicits user input on which beds need more soil and calculates the volume needed in units that the product is sold in.
    def soil(self):
        for s in bed:
            s = input('Which bed to do you need soil for?: ')
            print('You need ' + str(((self.length * self.width * self.depth)*self.depth)/27) + " cubic yards of soil") 
               
        
# solicits user input on the garden beds
beds = []
def getuserresponse():
    QN = input('What is the bed name? Enter "done" if finished:') 
    while QN != 'done':
        QL = input('What is the length of' + QN + '?: ')
        QW = input('What is the width of' + QN + '?: ')
        QD= input('What is the depth of' + QN + '?: ')
        QS= input('Does ' + QN + ' have shade, partial, or full sun?: ')
        QDr= input('Does ' + QN + ' have low, moderate, or high drainage?: ')
        Qpfd= input('What was the prior fertilization date? format 01/01/1999: ')
   
        beds.append(bed(QN, QL, QW, QD, QS, QDr, Qpfd))
        QN = input('What is the bed name?:') 

# writes the user input/class data to a file        
def save_beds():
    f = open('../data/beds.txt', 'a')
    f.write('store bed data here\n')
    getuserresponse() 

    for b in beds:
        f.write(b.name) #repeat for other properties
        f.write(b.length)
        f.write(b.width)
        f.write(b.depth)
        f.write(b.sun)
        f.write(b.drainage)
        f.write(b.pfd)












 


       



