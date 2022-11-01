# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, edited June 9 2021, accessed October 31 2022

from datetime import date, timedelta, datetime

class bed:
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='01/01/1999', pfd='01/01/1999', nfd='01/01/1999', finfd='01/01/1999'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = datetime.strptime(ffd, '%m/%d/%y')  #use datetime-strptime format 
        self.pfd = datetime.strptime(pfd, '%m/%d/%y') 
        self.nfd = datetime.strptime(nfd, '%m/%d/%y') 
        self.finfd = datetime.strptime(finfd, '%m/%d/%y')


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
        first_fert_date = date(2023, 5, 1)
        final_fert_date= date(2023, 10, 1)
        delta = timedelta(weeks=2)
        while first_fert_date <= final_fert_date:
            print(first_fert_date.strftime("%Y-%m-%d"))
            first_fert_date += delta

 #calculates the next fertilization date based on last date and recommended frequency
    def next_fert_date(self):
        delta = timedelta(weeks=2)
        while self.pfd <= self.finfd:
            print("The last fertilization was: " "\n" + self.pfd.strftime("%Y-%m-%d"))
            print("The next fertilization should be: ")
            self.pfd += delta
            break
   #calculates the size of the bed 
    def dimension(self):
        dimension=input(name + "is " + (length*width) + "sqft" )
        return dimension 

bed1 = bed()
bed2 = bed('bed2', 10, 4, 1, 'full', 'moderate', '2023, 5, 1', '2023, 9, 1', '', '2023, 10, 1' )  
bed3 = bed('bed3', 8, 3, 1, 'moderate', 'high', '2023, 5, 1', '2023, 9, 1', '', '2023, 10, 1')  
#how do I print this to file

print(bed.name)

bed2.fertilize_calendar
bed2.next_fert_date
bed2.dimension 

#Why does are my fert dates not recognized other than the one defined by a function?







 


       



