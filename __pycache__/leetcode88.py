#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def mergearray(a,m,b,n):
    l,r=0,0
    if n==0:
        return a
    else:   
        while l < len(a):
            if l<m:
                if a[l] < b[r]:
                    a[l]=a[l]
                    l+=1
                else:
                    a[l],b[r]=b[r],a[l]
                    l+=1
            else:
                if r<n:
                    a[l]=b[r]
                    r+=1
                    l+=1
                else:
                    l+=1
    return a
print(mergearray([1],1,[],0))