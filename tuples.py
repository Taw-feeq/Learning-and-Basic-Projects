import sys
import timeit

city=("pune","banglore","chennai","kolkata")

print(type(city))

print(city)
print(city[0])

village=("dolakpur","furfuri")
print(city+village)

locality=(city,village)
print(locality)

print(village*2)

#slicing
print(city[2:])

print(city[::-1])

#unpacking
sl=tuple("simplilearn")
print(sl)

a,b,c,d=city
print(a,b,c,d)
a, *b, c = city 
print(a,b,c)
a, *b, c = village
print(a,b,c)

del village
#print(village)      '''should give error'''

print(city.count("chennai"))

#converting list to a tuple
list=[1,2,3,4,5,6]
print(list)
print(type(list))

mytuple=tuple(list)
print(mytuple)
print(type(mytuple))

#size of list and tuple
print(sys.getsizeof(list),"bytes")          
print(sys.getsizeof(mytuple),"bytes")

#creation time of list and tuple
print(timeit.timeit(stmt="[123,456,789]",number=100000))
print(timeit.timeit(stmt="(123,456,789)",number=100000))
