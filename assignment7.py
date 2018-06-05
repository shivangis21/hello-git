#q1 area of sphere
r=float(input("Enter the radius"))
def funarea(r):
    area=4*3.14*r*r
    print(area)
funarea(r)

#q2 perfect number
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
          sum=sum+i

    if(sum==n):
        print(n)
for j in range (1,1001):
    perfect(j)

#q3 table of 12
def mul(n, i=1):
    if (i == 11):
        return 1
    else:
        print(n, "*", i, "=", n * i)
        return n * mul(n, i + 1)
mul(12)

#q4 Power of a number
def power(a,b):
    if(b==0):
        return 1
    else:
        pow = a * power(a,b-1)
        return pow

a=int(input("Enter value for a"))
b=int(input("Enter value for b"))
print(power(a,b))

#q5 Dictionary

d=dict()
def fact(n):
    if(n==1):
        return 1;
    else:
        return n * fact(n-1)
print(fact(3))
key=3
d[3]=fact(3)
print(d)




