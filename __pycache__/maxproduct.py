import math
#Given an integer array, the task is to find the maximum product of any subarray.

def maxproduct(a):
    product=1
    max1 = -math.inf
    for i in range(len(a)):
        product=max(a[i],product*a[i])
        max1 = max(max1,product)
    return max1
print(maxproduct([-2, 6, -3, -10, 0, 2]))
