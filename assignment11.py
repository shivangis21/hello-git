import _thread
import time
import math
import threading

#Q1
def printtime(threadn,delay):
    count=0
    while count<10:
        time.sleep(delay)
        count+=1
        print(threadn, time.ctime(time.time()))
try:
    _thread.start_new_thread(printtime("Thread1",5))
except:
    print("Thread can't be started")
while 1:
    pass
#Q2
import _thread
import time
def onetoten(threadn,delay):
    count=0
    while count<10:
        time.sleep(delay)
        count+=1
        print(count, time.ctime(time.time()))
try:
    _thread.start_new_thread(onetoten("Thread1",10))
except:
    print("Thread terminated")
while 1:
    pass

#q3
def printlis():
    list=(1,2,3,4,5)
    for i in range(len(list)):
        time.sleep(2*i)
        print(list[i],time.ctime(time.time()))
try:
    _thread.start_new_thread(printlis())
except:
    print("Thread terminated")
while 1:
    pass

#Q4
def factorial():

    n = int(input("Enter number:"))
    print("Factorial of the number is: ")
    print(math.factorial(n))
    time.sleep(2)

_thread.start_new_thread(factorial())
