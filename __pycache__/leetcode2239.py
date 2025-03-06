#Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

def findClosest(a):
    max=a[0]
    min=abs(a[0])
    i=0
    while i < len(a):
        if abs(a[i]) < min:
            min=abs(a[i])
            max=a[i]
            i+=1
        else:
            if abs(a[i])==min and a[i] >max:
                max=a[i]
            i+=1
    return max
print(findClosest([2,-1,12]))