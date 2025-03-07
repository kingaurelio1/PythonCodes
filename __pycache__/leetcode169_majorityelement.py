#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def MajorityElement(a):
    d={}
    for i in range(len(a)):
        d[a[i]]=0
    for j in range(len(a)):
        d[a[j]]+=1
    for k in range(len(a)):
        if d[a[k]]>len(a)//2:
            return a[k]
    return -1
print(MajorityElement([2,2,1,1,1,2,2,2]))
    