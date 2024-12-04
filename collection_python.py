from collections import Counter, namedtuple, defaultdict, deque

#Counter
string="aaaaaaaaaaaaabbbbbbbbbbbcccccdeffggghijjkkkkkkaaaaaaaaaaa"
s_count=Counter(string)
print(s_count)

print(s_count.items())
print(s_count.keys())
print(s_count.values())

print(s_count.most_common(2))
print(s_count.most_common(2)[0][0])

print(list(s_count.elements()))

#namedtuple
co_ordinates=namedtuple('Co_Ordinates', 'x,y,z')
co=co_ordinates(2,6,-3)
print(co)
print(co.x,co.y,co.z)

#defaultdict
dictionary=defaultdict(int)
'''
dictionary=defaultdict(float)
dictionary=defaultdict(list) '''
dictionary['a']=1
dictionary['b']=2
dictionary['c']=3
dictionary[4]='d'
dictionary[5]='e'
dictionary[6]='f' 
print(dictionary)
print(dictionary['c'])
print(dictionary[4])
print(dictionary['4'])
print(dictionary['g'])

#deque
queue=deque()
queue.append(2)
queue.append(3)
queue.appendleft(1)
queue.appendleft(0)
q=queue.copy()
print(queue)

queue.pop()
print(queue)
queue.popleft()
print(queue)

queue.clear()
print(queue)

queue.extend([1,2,3,4])
print(queue)
queue.extendleft([0,-1,-2,-3])
print(queue)

queue.rotate(1)
print(queue)
queue.rotate(2)
print(queue)
queue.rotate(-1)
print(queue)
queue.rotate(-2)
print(queue)

