#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
import time
def squared(a):
    start=time.time()
    left=0
    right=len(a)-1
    for i in range(len(a)):
        a[i]=a[i]**2
    while 0<right:
        if a[left]<a[right]:
            right-=1
        else:
            a[left],a[right]=a[right],a[left]
    end=time.time()
    return a,(1000*(end-start))
