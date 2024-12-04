import queue            #from queue import Queue

q=queue.Queue()         #q=Queue()

q.put("A")
q.put("B")
q.put("C")
q.put("D")
q.put("E")
q.put("F")
q.put("G")
q.put("H")
q.put("I")
q.put("J")

while not q.empty():
    print(q.get())
print("----------------END----------------")

p=queue.LifoQueue()         

p.put("A")
p.put("B")
p.put("C")
p.put("D")
p.put("E")
p.put("F")
p.put("G")
p.put("H")
p.put("I")
p.put("J")

while not p.empty():
    print(p.get())
print("----------------END----------------")

r=queue.PriorityQueue()

r.put((32, "T"))
r.put((2, "a"))
r.put((99, "w"))
r.put((45, "f"))
r.put((-62, "e"))
r.put((79, "e"))
r.put((-55, "q"))

while not r.empty():
    print(r.get()[1])

#                     deque
#       for deque refer collections.py file
#              and for the other type
#    there are simple queue and asychronous queue


#                       Methods available for each queue types
'''
queue.Queue	        - put(), get(), get_nowait(), task_done(), join(), empty(), full(), qsize()
queue.LifoQueue     - put(), get(), get_nowait(), task_done(), join(), empty(), full(), qsize()
queue.PriorityQueue - put(), get(), get_nowait(), task_done(), join(), empty(), full(), qsize()
collections.deque   - append(), appendleft(), pop(), popleft(), extend(), extendleft(), remove(),
                      rotate(), clear(), count(), reverse()
queue.SimpleQueue   - put(), get(), get_nowait(), empty(), qsize()
asyncio.Queue       - put(), get(), get_nowait(), task_done(), join(), empty(), qsize()
'''