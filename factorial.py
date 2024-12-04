def factorial(x):
    if x==1 or x==0:
        return 1
    else:    
        fact=x*factorial(x-1)
        return fact
x=int(input())
result=factorial(x)
print(result)


'''The above program to find factorial of a number is done by recursion method
    
                    The below progam is done using while loop'''


n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact = fact * n
    n -= 1  
print(fact)
