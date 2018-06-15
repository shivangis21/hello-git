import random
#Q1
f=open("File.txt","r+")
n=int(input("Enter the position from where you want to read the file:"))
f.seek(n,0)
print(f.read())
f.close()

#Q2
f6=open("Hello.txt")
s=f.read()
d=s.split()
print(d)
n=input("Enter the word to be counted: ")
if n in s:
 print(s.count(n))
f6.close()

#q3
f2=open("File.txt","r+")
data=f2.read()
f1=open("Hello.txt","w")
f1.write(data)
f2.close()
f1.close()

#q4
ff=open("new.txt","r")
f=open("second.txt","r")
p=ff.readlines()
t=f.readlines()
for i in range(len(p)):
 for j in range(len(t)):
    if(i==j):
      e=str(p[i])+str(t[j])
      print(e)
f.close()
ff.close()



#Q5
f5=open("file1.txt","r+")
for i in range(10):
    f5.writelines(str(i))
data=f5.read()
f5.close()
newdata=sorted(data)
file=open("New.txt","r+")
file.write(newdata)
file.close()

