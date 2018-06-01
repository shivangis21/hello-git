import queue

#Q1Creating a list
x = input("Enter value for x")
y = input("Enter value for y")
z = input("Enter value for z")
mylist = (x, y, z)
print(mylist)

#Q2Inserting a list
newlist=('google', 'apple', 'facebook', 'microsoft', 'tesla')
finallist=mylist+newlist
print("Final list is", finallist)

#Q3Couting occurences of element x
print(mylist.count(x))

#Q4Sorting list
numbers = ["89", "78", "65", "34", "67", "43", "2"]
numbers.sort()
print("Given array is", numbers)
print("The sorted numbers are", numbers)

#Q5Merging two arrays into a single array
a=["2", "6", "8", "9"]
b=["5", "10", "15"]
c=[a, b]
c.sort()
print(c)

#Q6Implement stack and queue using list
#stack
stack=[23, 42, 68]
stack.append(97)
c=0
o=0
print(stack)
for stac in stack:     #counting number of even/odd numbers in the stack
    if stac % 2==0:
        c=c+1
    if stac % 2!=0:
        o=o+1
print('Total even numbers are', c)
print('Total odd numbers are' , o)
while stack:  #Last element is popped first
    s=stack.pop()
    print('Element popped is',s)
#queue
q= queue
q=['Apple', 'banana', 'mango', 'papaya']
print(q)
q.append('berry')
print(q)
while q:
    j=q.pop(0)
    print('Element popped is', j) #Elements popped from front


