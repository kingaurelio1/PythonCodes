#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset=set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                hashset.remove(nums[i])
            else:
                hashset.add(nums[i])
        return next(iter(hashset))