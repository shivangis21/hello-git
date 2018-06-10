#Question1
class animal:
    def animalattribute(self):
        print("This is the method of base class")
class tiger(animal):
    def tiger(self):
        print("This is the method of inherited class")
t=tiger()
t.animalattribute()

#Question2

#A B
#A B

#Qustion3
class Cop:
   def __init__(self, name, age, work, exp, des):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.des = des

   def add(self, name, age, work, exp, des):
       self.name = name
       self.age = age
       self.work = work
       self.exp = exp
       self.des = des

   def display(self):
       print(self.name, self.age, self.work, self.exp, self.des, sep = '\n')

   def update(self, name, age, work, exp, des):
       self.name = name
       self.age = age
       self.work = work
       self.exp = exp
       self.des = des

class Mission(Cop):
       def add_mission_details(self):
        print('Available for mission')

m = Mission('Raj', 26, 'field', 2, 'Junior\n')
m.display()
m.add('Mohan', 35, 'Armoury', 9, 'Colonel\n')
m.display()
m.update('Amit', 25, 'Inventory', 4, 'Intern\n')
m.display()
m.add_mission_details()

#Question4
class shape:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        print("The area is:", area)
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
class square(shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
r=rectangle(10,20)
r.area()
s=square(10,10)
s.area()