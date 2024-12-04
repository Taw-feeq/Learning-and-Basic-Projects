'''
The function accepts two integers n, m as arguments Find the sum of all numbers in range from 
1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers 
not divisible by n with sum of numbers divisible by n.
'''
def diffSum(divisor, number):
    divisible_n = 0
    not_divisible_n = 0
    for i in range(1, number+1):
        if i % divisor == 0:
            divisible_n += i
        else:
            not_divisible_n += i
    return (not_divisible_n - divisible_n)

n, m = map(int, input("Enter the Divisor and the range of numbers: ").split())
print(diffSum(n,m))