#q1 Input 10 elements
list = []
for i in range(10):
    x = int(input("Enter the element \n"))
    list.append(x)
    i += 1
for i in range(len(list)):
    print(list[i])

#q2 Infinite Loop
while(1):
    print("Infinite")

#q3 squares of element
lis= []
n=int(input("Enter total number of elements"))
for i in range(n):
    x = int(input("Enter the element \n"))
    lis.append(x)
for i in range(len(lis)):
    lis[i]=lis[i]*lis[i]
for i in range(len(lis)):
    print(lis[i])

#q4 seperating data types
data=[1,2,3.0,"apple",5.6,"Banana"]
intl=[]
floatl=[]
stril=[]
for x in range(len(data)):
    intl= list(filter(lambda x: (type(x)==int) , data))
    floatl=list(filter(lambda x: (type(x)==float),data))
    stril=list(filter(lambda x: (type(x)==str), data))
print(intl)
print(floatl)
print(stril)

#q5 prime number
pri=[]
for p in range(1,101):
    k=0
    for i in range(2,p//2+1):
        if(p%i==0):
            k=k+1
    if(k<=0):
        pri.append(p)
print(pri)


#q6 pattern
for i in range(0,4):
    for j in range(0,i+1):
        print("*", end=" ")
    print('\n')

#q7 dictionary
my_dict = dict()
n=int(input("Enter number of elements"))
for i in range(n):
 key = input("Enter the key: ")
 value = input("Enter the value: ")
 my_dict[key] = value
for k in my_dict:
    print(my_dict[k])

#q8
dell = []
n = int(input("Enter total number of elements"))
for i in range(n):
    x = input("Enter the element \t")
    dell.append(x)
o = int(input("Enter element to be deleted"))
for i in range(len(dell)):
    if dell[i] == o:
        del dell[i]
for i in range(len(dell)):
    print(dell[i])




