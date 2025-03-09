from collections import deque
def ReverseQueue(queue,k):
    l=[]
    i=0
    t=len(queue)-k
    while i < k:
        l.append(queue.popleft())
        i+=1
    for j in range(len(l)-1,-1,-1):
        queue.append(l[j])
    while t>0:
        key=queue.popleft()
        queue.append(key)
        t-=1
    return queue
d = deque([1, 2, 3, 4,5,6])
print(ReverseQueue(d,3))