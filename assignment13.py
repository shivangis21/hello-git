#q1
#Zero division error
a=3
try:
 if a<4:
   a=a/(a-3)
   print(a)
except ZeroDivisionError:
 print("Error!")


#q2
#Out of index error
l=[1,2,3]
try:
 print(l[3])
except IndexError:
 print("Error!")

#q3
#Output
#An exception will be raised
'''
An exception
Traceback (most recent call last):
  File "C:/Users/Shivangi/PycharmProjects/Project1/trial.py", line 4, in <module>
    raise NameError("Hi there")  
NameError: Hi there
'''

#q4
'''
-5.0

a/b result in 0
'''

#q5
try:
 import Error
except ImportError:
 print("Error! Not imported")

try:
 l=[1,2,3]
 print(l[3])
except IndexError:
 print("Error! Out of Index")

try:
   s=int(input("enter an integer"))
   print(s)
except ValueError:
 print("Error! Value Error")

 #q6
class AgeTooSmallError(Exception):
   pass
while(1):
 s =int(input("Enter your age"))
 try:
  if s < 18:
   raise AgeTooSmallError
  else:
   print("Correct Age!")
   break
 except AgeTooSmallError:
   print("Your age is small")

