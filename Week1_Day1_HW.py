#Week 1 Certificate
#Day 1 Numbers
import datetime
from  datetime  import date

#Number of hours in a Year
No_of_hours = 365 * 24
print("Number of Hours in a year: ", No_of_hours)

#Number of Minutes in a Decade
No_of_Mins_Dec = 10 * 365 * 24 * 60 
print("Number of Minutes in a Decade: ", No_of_Mins_Dec)

#My age in seconds
No_of_Sec = 39*365*24*60*60
print("Number of Secondas:", No_of_Sec)


#Calculating Andreas Age from seconds
Number_of_Mins =  48618000/60
Number_of_hours  = Number_of_Mins/60
Number_of_days  = Number_of_hours/24
Number_of_Years = Number_of_days/365
print("Andreea's Age", Number_of_Years)

# Number of days for a  32-bit system to timeout
# maximum positive value of a signed 32 bit integere is 2 ** 31 - 1 = 2147483647
# Assuming 1 integer value to fade every 1 second

No_Timeout = 2 ** 31 - 1 // (60 * 60 * 24)
print(2 ** 31 - 1)
print ("No of days to timeoutfor a 32 bit integer: ", No_Timeout)

No_Timeout = 2 ** 63 - 1 // (60 * 60 * 24)
print(2 ** 63 - 1)
print ("No of days to timeout for a 64 bit integer: ", No_Timeout)

#Calculate age
Difference  = datetime.datetime.now() - datetime.datetime(1978,10,9,15,0,0)

#Age = abs(Difference/365)
print("My Age:", Difference)




