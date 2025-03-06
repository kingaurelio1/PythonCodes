#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def Rotate(a,k):
    k=k%len(a)
    l,r=0,len(a)-1
    while l < r:
        print(a)
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    l,r=0,k-1
    while l<r:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    l,r=k,len(a)-1
    while l < r:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    return a
print(Rotate([1,2,3,4,5],2))