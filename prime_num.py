#to find the first n prime numbers

def prime(n):
    if n<=1: return False
    for i in range (2, n//2 + 1):
        if n%i == 0:
            return False
    return True

num = int(input("Enter the number of prime numbers you want to print: "))
i = 2
list = []
while True:
    if prime(i):
        list.append(i)
        if len(list) == num:
            break
    i+=1

print(list)