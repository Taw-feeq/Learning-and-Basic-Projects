import math

def square(i):
    sqrt = math.isqrt(i) 


def plot(n,a):
    if n == len(a):
        list=[]
        for i in a:
            x=i
            sqrt_chk = square(i)
            list.append(sqrt_chk)
        print(len(list))
        

n=int(input("Enter the number of plots:"))
a=[int(x) for x in input("Enter the size of the plots:").split()]
plot(n,a)
