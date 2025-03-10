#Given an array arr[] of size n, the task is to rearrange it in alternate positive and negative manner without changing the relative order of positive and negative numbers. In case of extra positive/negative numbers, they appear at the end of the array.
from collections import deque
def Alternating(a):
    positives=deque()
    negatives=deque()
    l=[]
    for i in range(len(a)):
        if a[i]>=0:
            positives.append(a[i])
        else:
            negatives.append(a[i])
    counter=0
    print(positives,negatives)
    while counter < len(a):
        if len(positives)==0 and len(negatives)>0:
            l.append(negatives.popleft())
        elif len(negatives)==0 and len(positives)>0:
           l.append(positives.popleft())
        elif counter%2==0 and positives:
            l.append(positives.popleft())
        elif counter%2==1 and negatives:
            l.append(negatives.popleft())
        counter+=1
    return l
print(Alternating([1, 2, 3, -4, -1, -14,-16,-7]))