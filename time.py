import datetime as dt
from datetime import date

print (date.today())
print(dt.datetime.now().time())
print(dt.datetime.today().weekday())
print(dt.datetime.now().weekday())

Current_Date = dt.datetime.today()
print ('Current Date: ' + str(Current_Date))

Previous_Date = dt.datetime.today() - dt.timedelta(days=1)
print ('Previous Date: ' + str(Previous_Date))

NextDay_Date = dt.datetime.today() + dt.timedelta(days=1)
print ('Next Date: ' + str(NextDay_Date))