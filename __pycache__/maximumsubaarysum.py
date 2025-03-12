#Given an integer array nums, find the subarray with the largest sum, and return its sum.
import math 
def maxsum(a):
    l,sum,r=0,0,1
    max1 = -math.inf
    for i in range(len(a)):
        sum=max(a[i],sum+a[i])
        max1 = max(max1,sum)
    return max1
print(maxsum([-2,1,-3,4,-1,2,1,-5,4]))

