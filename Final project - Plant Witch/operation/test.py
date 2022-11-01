

from datetime import date, timedelta

start_date = date(2023, 5, 1)
end_date = date(2023, 10, 1)
delta = timedelta(weeks=2)
while start_date <= end_date:
    print(start_date.strftime("%Y-%m-%d"))
    start_date += delta


   def fert_date(self):
        last_fert_date = date()
        next_fert_date = date()
        final_fert_date = date(2023, 10, 1)
        delta = timedelta(weeks=2)
        while last_fert_date <= final_fert_date:
            print(last_fert_date.strftime("%Y-%m-%d"))
            last_fert_date += delta

bed = bed()
bed2 = bed('bed2', 10, 4, 1, 'full', 'moderate', '2023, 9 7', ''  )

print (bed2.sun)

bed2.fert_date