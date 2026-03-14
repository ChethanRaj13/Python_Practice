# WAP to Define a circle class create the cirle with constructure taking radius r
# define Area() method for the class to find the area of the circle
# define Perimeter() method to find the perimeter of circle

class Circle:
    
    def __init__(self, rdx):
        self.rdx = rdx

    def Area(self):
        return 3.14 * (self.rdx ** 2)
    
    def Perimeter(self):
        return 2 * 3.14 * self.rdx
    

c1 = Circle(14)
area = c1.Area()
peri = c1.Perimeter()
print(area,peri)

#--------------------------------------------------------------

# define a Empolyee class with attributes role, department and salary 
# have a showdetail() methord to print all the detail
# create an inheritent class called Engineer and have attribute name and age

class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetail(self):
        print("role:",self.role,"\ndeptartment:",self.dept,"\nsalary",self.salary) 

class Engineer(Employee):

    def __init__(self,role,dept,salary,name,age):
        self.name = name
        self.age = age
        super().__init__(role,dept,salary)

e1 = Engineer("SDE1","tech","20LPA","rohit","30")
e1.showdetail()

#--------------------------------------------------------------

# create a class called order which stores item and price
# use dunder function __gt__() to convert order1 > order2 if the price of order1 > price of order 2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price
    
o1 = Order("tea",30)
o2 = Order("coffee",40)
print(o2>o1)            