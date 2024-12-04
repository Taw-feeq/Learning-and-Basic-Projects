'''
class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
        print("__init__ works without calling")
    def display(self):
        print("Name:",self.name)
        print("Reg No:",self.regno)
t1=teacher("Gayathri",679)      # print statement in the init function will be printed 
t2=teacher("Jayanthi",465)      # while defining the object 

t1.display()
t2.display() 
'''

class calc:
    sum=100    #class variable
    
    def __init__(self, num1,num2):
        self.a=num1             #Instance variable
        self.b=num2             #Instance variable
   
    def add(self):              #Instance method(Function)
        print("Addition of two numbers is:",self.a+self.b)
    def sub(self):
        print("Subraction of two numbers is:",self.a-self.b)
    def mul(self):
        print("Multiplication of two numbers is:",self.a*self.b)
    def div(self):
        print("Division of two numbers is:",self.a/self.b)
    
    @classmethod                #Class method(Function)
    def result(cls):
        cls.sum=999
        print(cls.sum)
    
    @staticmethod               #Static method(Function)
    def random():
        print("This is static method")

obj1=calc(10,2)
obj2=calc(98,23)

obj1.add()
obj1.sub()
obj2.mul()
obj2.div()

calc.result()           #calc.result(calc)      #calling of class method using the class name

obj1.random()           # static method can be called using both the class 
calc.random()           # aswell as the object of the class




