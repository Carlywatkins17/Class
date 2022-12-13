# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, edited June 9 2021, accessed October 31 2022

from datetime import date, timedelta, datetime
import _strptime


class bed:
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='05/01/2023', pfd='07/20/2022', finfd='09/15/2023'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = datetime.strptime(ffd, '%m/%d/%Y')  
        self.pfd = datetime.strptime(pfd, '%m/%d/%Y') 
        self.finfd = datetime.strptime(finfd, '%m/%d/%Y') 
        
    def toJSON(self):
        return self.__dict__ 


 # I thought this datetime.strptime would work better.  If I enter a single digit day, it will convert that, but it will not convert a 2 digit year.  It will error out
 # I would like top be able to format more intuitively and remove the formatting instructions printed in the input feilds of getuserresponse().       



 


       



