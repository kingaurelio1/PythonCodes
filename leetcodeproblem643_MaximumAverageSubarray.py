#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

def MaxSubarryAverage(nums,k):
    l=0
    currentsum=0
    maxsum=float('-inf')
    for i in range(len(nums)):
        currentsum+=nums[i]
        if ((i-l+1)==k):
            maxsum=max(currentsum,maxsum)
            currentsum-=nums[l]
            l+=1
    return maxsum/k