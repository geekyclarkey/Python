
from datetime import datetime

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
year = int(year)
day = int(day)
month = int(month)

#these months have 30 days all the rest have 31 (except feb)
thirty = [4, 6, 9, 11]

if month == 2:
  if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            month = 29
        else:
            month = 28
    else:
        month = 29
  else:
    month = 28
elif month in thirty:
  month = 30
else:
  month = 31

def calculate():
    subs = float(input("\nWhat is the subscription amount? ")) #Float is so we can input decimal points
    days_left = month - day + 1
    total = (subs/month)*days_left
    result = ("%.2f" % total) #This rounds the number to 2 decimal places. Just like curency.

    print (f"""
The amount to pay, to take the subscription
to the end of the current month is:
{result} Euros""")

while 1 == 1:
    calculate()
