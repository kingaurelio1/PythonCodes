#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def duplicate(l):
    right=len(l)-1
    t=False
    for left in range(len(l)):
        while left < right:
            if l[left] != l[right]:
                right-=1
            else:
                t=True
                break
    return t

print(duplicate([1,2,3,4]))