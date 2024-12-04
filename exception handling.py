try:
    x = int(input())
    y = int(input())
    z = input()
    
    a = x + y
    b = z + x

except TypeError:
    print("Error: cannot add an int and a str")
except ValueError as v:
    print("Value Error", v)
except NameError as n:
    print("Name Error", n)
except SyntaxError as s:
    print("Syntax Error", s)

except Exception as e:
    print("Error Occurred", e)

finally:
    print("The program is successfully executed")

class valuetoohigherror(Exception):
    print("OO")
    pass

def power(x):
    if x < 100:
        print(x**2)
    else:
        raise valuetoohigherror("Number must be below 100")

try:
    power(125)
except valuetoohigherror as e:
    print(e)