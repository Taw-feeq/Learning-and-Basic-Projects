import random
from functools import reduce
add = lambda x : x + random.randint(1,100)
mul = lambda x, y : x*y
print(add(12))
print(mul(4,8))

point=[(1,2),(5,5),(2,-4),(9,2),(8,4),(3,5)]
point_sort=sorted(point)
point_sorted=sorted(point, key=lambda x: x[1])
print(point)
print(point_sort)
print(point_sorted)

def sort_pt(x):
    return x[0] + x[1]

point_srt=sorted(point, key=sort_pt)        #point_srt=sorted(point, key=lambda x: x[0] + x[1])
print(point_srt)

#map function
a=[9,7,4,2,3,1,8]
b=map(lambda x: x**2, a)
print(list(b))

#filter function
a=[9,7,4,2,3,1,8]
b=filter(lambda x: x%2==0, a)
print(list(b))

#reduce function
a=[1,2,3,4,5,6,7,8,9]
b=reduce(lambda x,y:x*y , a)
print(b)

