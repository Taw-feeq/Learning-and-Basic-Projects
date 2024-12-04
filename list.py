a=[1,2,3,4,5,6,7,330]
two, *other=a
a.append(8)
print(a)
a.remove(7) #removes the specified value and not the index
print(a)
a.pop(3)   #removes the value in that specific index
print(a)
a.insert(6,7)
print(a)
print(sum(a))

b=[0]
a.extend(b)
print(a)
a.sort()
print(a)

#insert a list of values into another list at a specific index

insert_list = ['a', 'b', 'c']
insert_index = 2

for item in insert_list: 
    a.insert(insert_index, item)
    insert_index+=1
print(a)

#removes a list of values 

elements_to_remove = [2, 5, 8,'a', 'b', 'c']
a = [x for x in a if x not in elements_to_remove]
print(a)