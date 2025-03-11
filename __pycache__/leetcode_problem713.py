#Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

#Primera idea
def subbaray(a,k):
    num=0
    #for i in range(len(a)):
        #if a[i] < k:
            #num+=1
    l=0
    r=1
    product=a[l]
    while r < len(a):
        if product < k:
            product*=a[r]
            r+=1
            num+=1
        else:
             l+=1
             r=l+1
             product=a[l]
    return num
print(subbaray([1,2,3,4,5,6],50))

#Segunda idea
