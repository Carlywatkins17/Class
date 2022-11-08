from datetime import date, timedelta, datetime


class bed:
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='01/01/1999', pfd='01/01/1999', n_f='01/01/1999', finfd='01/01/1999'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = ffd
        self.pfd = pfd
        self.n_f = n_f
        self.finfd = finfd
  
        
      
        

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
        self.ffd = datetime.strptime(self.ffd, '05/1/2023')
        self.finfd= datetime.strptime(self.finfd, '01/10/2023')
        delta = timedelta(weeks=2)
        while self.ffd <= self.finfd:
            print(self.ffd.datetime.strptime('%m/%d/%Y'))
            self.ffd += delta

bed1 = bed('bed1', 10, 2, 1, 'mild', 'high', '05/01/2023', '06/02/2023', '', '10/01/2023')

bed1.fertilize_calendar
 #calculates the next fertilization date based on last date and recommended frequency
    #def nfd(self):
        #delta = timedelta(weeks=2)
       # while self.pfd <= self.finfd:
            #next = self.pfd + delta
           # return next
            #break
                                             

   #calculates the size of the bed 
   # def size(self):
       # size=input(self.name + "is " + (self.length*self.width) + "sqft" )
       # return size 

#bed1 = bed()
#bed2 = bed('bed2', 10, 4, 1, 'full', 'moderate', '01/05/2023', '09/02/2023', '', '10/02/2023')  
#bed3 = bed('bed3', 8, 3, 1, 'moderate', 'high', '05/01/2023', '09/03/2023', '', '10/01/2023')  
#how do I print this to file

#print(bed2.name)
#print(bed2.sun)
#print(bed2.finfd)
#bed2.nfd()
