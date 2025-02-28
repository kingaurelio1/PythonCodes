#Given a binary array arr[] and an integer k, find the maximum length of a subarray containing all ones after flipping at most k zeroes to 1’s.

def maxzeros(l,k):
    left=0
    right=0
    sum=0
    t=0
    while right<len(l):
        print(left,right,sum,t)
        if l[right]==0:
            t+=1
        while t>k:
            if l[left]==0:
                t-=1
            left+=1
        sum=max(sum,right-left+1)
        right+=1
    return sum
print(maxzeros([1,0,1],1))