import itertools
import operator

#Product
a=[1,2,3]
b=[4,5]
product= itertools.product(a,b)
print(list(product))

a=[1,2]
b=[4]
product= itertools.product(a,b, repeat=2)
print(list(product),'\n')

#Permutation
a=[1,2,3]
permutation=itertools.permutations(a)
print(list(permutation))
permutation=itertools.permutations(a,2)
print(list(permutation),'\n')

#Combination
a=[1,2,3,4,5]
combination=itertools.combinations(a,3)
print(list(combination))
combination=itertools.combinations(a,5)
print(list(combination))

comb_wr=itertools.combinations_with_replacement(a,2)
print(list(comb_wr),'\n')

#Accumulate
a=[1,2,3,4,5]
acc= itertools.accumulate(a)
print(a)
print(list(acc),'\n')

#Multiply
acc1= itertools.accumulate(a, func=operator.mul)
print(list(acc1),'\n')

#Max
a=[1,2,3,8,4,5]
acc1= itertools.accumulate(a, func=max)
print(list(acc1),'\n')

#Groupby
def summa(n):
    return n>18  

a=[1,4,7,9,12,16,21,25]
group=itertools.groupby(a,key=summa)
for k,v in group:
    print(k,list(v))

employees=[ ("Victoria", "IT"), ("Carl", "SDE"), ("Billy", "IT"), ("Hughie", "SDE"), ("Anthony", "ML") ]

group_by_dept=itertools.groupby(employees, key=lambda x : x[1])
for dept , emp in group_by_dept:
    print(dept, list(emp))
print("-------------------------------")

ordered_employees=sorted(employees, key=lambda x : x[1])
group_by_dept=itertools.groupby(ordered_employees, key=lambda x : x[1])
for dept , emp in group_by_dept:
    print(dept, list(emp))
print("-------------------------------")

emp_dict={}
for name, department in employees:
    if department in emp_dict:
        emp_dict[department].append(name)
    else:
        emp_dict[department]=[name]
for department, names in emp_dict.items():
    print(department, names)
print("-------------------------------")

#count
for i in itertools.count(10):       #count(10, step=3) with step value 3    O/P:10,13,16,.....
    print(i)
    if i == 12:                     #without a stop condition it goes on infinitively
        break

#cycle
'''
a=[1,2,3,8]
for b in itertools.cycle(a):
    print(b)
'''

#repeat
a=[1,2,5]
for b in itertools.repeat(7, 3):
    print(b)