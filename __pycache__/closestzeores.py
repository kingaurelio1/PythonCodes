
def findClosestNumber(nums):
    min1=float('inf')
    max1=float('inf')
    for i in range(len(nums)):
        if abs(nums[i]) < min1:
            min1=abs(nums[i])
            max1=nums[i]
        else:
            if abs(nums[i])==min1:
                max1=max(max1,nums[i])
    return max1
        

print(findClosestNumber([2,-1,1]))