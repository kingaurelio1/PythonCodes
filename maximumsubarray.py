#Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maximumsubarray(l):
    n=len(l)
    max=0
    left=0
    right=1
    maxnum=0
    sum=0
    if len(l)==1:
        return l[0]
    else:
        while right < len(l):
            sum+=l[left]
            if sum < sum+sum[right]:
                right+=1
                left+=1
            
    return None

