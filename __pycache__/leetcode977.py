#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
import time
def squared(a):
    l,r=0,len(a)-1
    t=[0]*len(a)
    i=len(a)-1
    while l <= r:
        if a[l]**2 > a[r]**2:
            t[i]=a[l]**2
            l+=1
            i-=1
        else:
            t[i]=a[r]**2
            r-=1
            i-=1
    return t
print(squared([-7,-3,2,3,11]))