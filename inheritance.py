class a():
    def __init__ (self):                #base class/parent class
        print("A")
    
    def display (self): 
        print("you are in class a")

class b(a):                             #single inheritance
    def __init__ (self): 
        super().__init__()              #super keyword is used to call the constructor of the parent class
        print("B")

    def display(self): 
        print("you are in class b")

class c(b,a):                           #multiple inheritance and multilevel inheritance
    def __init__ (self):
        super(). __init__()
        print("c")
        
    def display (self): 
        print("you are in class c")

class d(a):                             #hierarchy inheritance
    pass    

class e(a):                             #hierarchy inheritance
    pass

class f(a):                             #hierarchy inheritance
    pass

class g():
    print("Hybrid")

class h(a):                             #hybrid inheritance
    pass

class i(a,g):                           #hybrid inheritance
    pass

obl=h()
obl.display()

