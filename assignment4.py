#Tuples
#Q1 Finding length of a tuple
t=('add','23','item','0.5')
print(t)
print('Length of the tuple is',len(t))

#Q2 Maximum and minimum element in a tuple
print('Biggest element in the tuple is', max(t))
print('Smallest element in the tuple is', min(t))

#Q3 Product of all elements in a tuple
p=1
tuple=(2,3,4,5)
print(tuple)
for t in tuple:
        p = p * t
print('Product of elements of tuple is:',p)

#Sets
#Q1
x=input('Enter value for x')
y=input('Enter value for y')
z=input('Enter value for z')
a=input('Enter value for a')
b=input('Enter value for b')
c=input('Enter vaue for c')
set1=set([x,y,z])
set2=set([a,b,c])
print('Set 1 is', set1)
print('Set 2 is', set2)
set4=set1 | set2
print('The difference of two sets is', set4)
print('The comparison of two sets is',)
set3= set1 & set2
print('The intersection of two sets is', set3)

#Dictionaries
#Q1 student dictionary
my_dict = dict()
for i in range(10):
 key = input("Enter the key(name): ")
 value = input("Enter the value(marks): ")
 my_dict[key] = value
print(my_dict)


#Q2 Sorting dictionary on basis of marks
print(sorted(my_dict, key=my_dict.get))



#Q3
src=['MISSISIPI']
src=['M','I','S','S','I','S','I','P','I']
result_dict = dict( [ (i, src.count(i)) for i in set(src) ] )
print(result_dict)

