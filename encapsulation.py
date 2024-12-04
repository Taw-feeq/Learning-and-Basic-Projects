class company:                                      #Access Modifiers
    def __init__(self):
        self.companyname="GOOGLE"                   #Public Variable 
        self.__salary = 200000                      #Private Variable   using   __
        self._jobrole = "Software Engineer"         #Protected Variable using   _
    
    def salary(self):
        print(self.__salary)                        #private variable can be called only inside the class

class employee(company):
    def job(self):
        super().__init__()                          #protected variable can be called in any class 
        print(self._jobrole)                        #related with the parent class (inheritance)

e1=employee()
print(e1.companyname)                               #public variable can be called anywhere in the program
e1.salary()
e1.job()

