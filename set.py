myset={1,2,3,4,5,2,4,6,7,8}
print(myset)
print(type(myset))

myset1={}
print(type(myset1))

myset2=set()
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)

myset.remove(6)
print(myset)

myset.discard(6)
print(myset)

myset.discard(5)
print(myset)

print(myset.pop())
print(myset)

newset=myset.copy()

myset.clear()
print(myset)

odd={1,3,5,7,9}
even={2,4,6,8,10}
prime={2,3,5,7}

union=odd.union(even)
print(union)

inter=odd.intersection(prime)
print(inter)

setA={1,2,3,4,5,6,7,8,9,10}
setB={2,4,6,12,16,18}

diff=setA.difference(setB)
print(diff)

diff=setB.difference(setA)
print(diff)

setA.difference_update(setB)
print(setA)

diff=setA.symmetric_difference(setB)
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))

fset=frozenset([1,2,3,4,5])
print(fset)

f2set=frozenset({1,2,3,4,5})
print(f2set)

fsetA=frozenset(setA)
print(fsetA)

