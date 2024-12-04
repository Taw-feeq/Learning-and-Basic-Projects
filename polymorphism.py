'''
class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):                      
    def sound(self):                         #Method Overridding
        print("Dog Barks")

class bird(animal):
    def sound(self):                         #Method Overridding
        print("Bird sings")

d1=dog()
d1.sound()

b1=bird()
b1.sound()


class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self,a,b):
        print("Area of a Rectangle is:",a*b)

r1=rectangle()
r1.area(10,20)
'''

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept=dept
    
    def display(self):
        print(self.name,self.salary,self.dept)
        print(f"{self.name,self.salary,self.dept}")

m1=manager("Tawfeeq", 100000, "SDE")
m1.display()