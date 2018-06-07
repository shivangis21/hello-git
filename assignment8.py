import time
import datetime
from datetime import date
import os
import math

#q1
#Python Stores time in form of tuples. It is made up of nine tuples. These tuples store different values related to time
#like year, month, date etc.

#q2
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

#q3
now = datetime.datetime.now()
print( now.month)

#q4
now = datetime.datetime.now()
print( now.day)

#q5
n = date.today()
print("The date is",n)
print("The date is",n.day)


#q6
localtime = time.localtime(time.time())
print("Local current time :", localtime)

#q7
num=int(input("Enter the number"))
print("The factorial of number is", math.factorial(num))

#q8
m=int(input("Enter a number"))
n=int(input("Enter a number"))
print("GCD of two number is",math.gcd(n,m))

#q9
print(os.getcwd())
print(os.name)