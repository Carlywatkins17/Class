from createbeds import bed 
from datetime import date, timedelta, datetime
import _strptime
from beduserinput import beds

#referenced stack overflow user Burnash "Iterating through a range of dates in python" edited code to my specifications.
# from datetime import date, timedelta
#start_date = date(2019, 1, 1)
#end_date = date(2020, 1, 1)
#delta = timedelta(days=1)
#while start_date <= end_date:
#    print(start_date.strftime("%Y-%m-%d"))
#    start_date += delta

#creates a calendar of that years recommended fertilization dates for that bed
# If I say "for b in bed (the class) then I get an iteration error.  If I write "For b in beds(the list) it will print me a calendar, based on the last item I put in the list. 
#if I entered more than one bed before I wrote "done" it processes for both.
#if I enter a bed from the txt file that wasnt the last thing I entered, I get the calendar for the last thing I entered. 
#How do I call on the txt file as the list here?  

def fert_cal():
    delta = timedelta(weeks=2)
    # b = input('Which bed do you need the size of?') #this line is not functioning as intended
    
    for b in beds:
        print('Here is your fertilization calendar: ')
        start_date = b.ffd
        end_date = b.finfd
        while start_date <= end_date:
            print(start_date)
            start_date += delta 

#def fert_cal():
    #delta = timedelta(weeks=2)
    #print('Here is your fertilization schedule: ')
    #for b in beds:
    #    start_date = b.ffd
     #   end_date = b.finfd
      #  while start_date <= end_date:
       #     print(start_date)
        #    start_date += delta 
                            

 # calculates the next fertilization date based on last date and recommended frequency 

def nfd():
    delta = timedelta(weeks=2)
    print('Here is your fertilization schedule: ')
    for b in beds:
        start_date = b.pfd
        end_date = b.finfd
        while start_date <= end_date:
            print(start_date)
            start_date += delta

            