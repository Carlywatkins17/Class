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

    def fertilize_calendar(self):
        delta = timedelta(weeks=2)
        while self.ffd <= self.finfd:
            print(self.ffd)
            self.ffd += delta

 # calculates the next fertilization date based on last date and recommended frequency
    #def nfd(self):
        #delta = timedelta(weeks=2)
        #if self.pfd <= self.finfd:
            #next = self.pfd + delta
            #print(next)  
                         
    def nfd(self):
        delta = timedelta(weeks=2)
        while self.pfd <= self.finfd: 
            text=input("The next fertilize date is: " + str(self.pfd + delta))
            return text
            
            
   #calculates the size of the bed 
    def dimension(self):
        dimension=input(self.name + " is " + str(self.length*self.width) + " sqft" )
        return dimension 

bed1 = bed('bed1', 8, 3, 1, 'light', 'low', '01/05/2023', '09/01/2023','10/01/2023')
bed2 = bed('bed2', 10, 4, 1, 'full', 'moderate', '01/05/2023', '09/02/2023', '10/01/2023')  
bed3 = bed('bed3', 8, 3, 1, 'moderate', 'high', '05/01/2023', '09/03/2023', '10/01/2023')  
#how do I print this to file

print(bed1.name)
print(bed1.sun)
print(bed1.finfd)
bed1.fertilize_calendar()
bed1.dimension()
bed1.nfd()

f = open('../data/beds.txt', 'a')
f.write('# Measure and name beds, create classes and behaviors')











 


       



