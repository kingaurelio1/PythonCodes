#Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

#You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        for j in range(len(nums)):
            if hashmap[nums[j]]==1:
                return nums[j]