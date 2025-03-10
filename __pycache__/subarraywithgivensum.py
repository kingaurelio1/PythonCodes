#Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

def subarray(a,s):
    l=0
    r=1
    sums=a[0]
    while r<len(a):
        if sums < s:
            sums+=a[r]
            r+=1
        elif s < sums:
            l+=1
            r=l+1
            sums=a[l]
        elif sums==s:
            return [l+1,r]
    return -1
print(subarray([15, 2, 4, 8, 5, 10],23))