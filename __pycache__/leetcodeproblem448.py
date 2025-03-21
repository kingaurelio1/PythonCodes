#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

#Primera Idea
def missingnumbers(nums):
    list1=[]
    hashset=set()
    for i in range(len(nums)):
        hashset.add(nums[i])
    for j in range(1,len(nums)+1):
        if j not in hashset:
            list1.append(j)
    return list1
#Se resuelve en tiempo lineal pero se resuelve en espacio lineal