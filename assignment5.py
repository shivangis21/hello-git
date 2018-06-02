#Q1 To check if it's leap year or not
year=int(input("Enter a year"));
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It's a leap year")
else:
    print("Not a leap year")

#Q2 Checking dimensions of square and rectangle
length=input("Enter the length")
breadth=input("Enter the breadth")
if(length==breadth):
    print("Dimensions are of square")
else:
    print("Dimensions are of rectangle")

#Q3 comparison of ages
a=input("enter age of first person")
b=input("enter age of second person")
c=input("enter age of third person")
if(a>b):
    if(a>c):
        print("A is the eldest")
    else:
        print("C is the eldest")
elif(b>a):
    if(b>c):
        print("B is the eldest")
    else:
        print("C is the eldest")

#Q4 Employee database
age=int(input("Enter your age"))
gender=input("Enter your gender(F/M)")
m=input("Enter your marital status(Y/N)")
if(gender=="F"):
    print("Employee to work in only urban areas")
elif((gender == "M")&(age > 20 or age < 40)):
    print("Employee can work anywhere")
elif((gender=="M")&(age>40 or age<60)):
    print("employee to work only in urban areas")
else:
    print("Error")

#Q5 Discount problem
quant=int(input("Enter the quantity purchased"))
cost=quant*100
print("Total cost is", cost)
discount=(10*cost)/100
if(cost>1000):
    print("Discount offered!")
    cost=cost-discount
    print("Cost for the user after discount is", cost)
else:
 print("No discount offered")
 print("Cost remains", cost)



