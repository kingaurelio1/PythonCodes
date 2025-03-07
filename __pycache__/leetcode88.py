#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
def mergearray(a,m,b,n):
    l,r=0,0
    c=[]
    if n==0: return a
    elif m==0: return b
    else:
        l,r=0,0
        temp=0
        while l<m:
            if r<n:
                if a[l] < b[r]:
                    c.append(a[l])
                    l+=1
                else:
                    c.append(b[r])
                    r+=1
            else:
                if a[l]!=0:
                    c.append(a[l])
                    l+=1
                else:
                    l+=1
    if r < n:
        while r < n:
            c.append(b[r])
            r+=1
    return c
print(mergearray([1,2,3,0,0],3,[-3,-1],2))
#Resuelto en una complejidad de tiempo O(m+n) pero no O(m+n) espacial

def mergearray2(a,m,b,n):
    l,r=0,0
    if n==0: return a
    elif m==0: return b
    else:
        while r < n:
            a[m+r]=b[r]
            r+=1
        if a[m]>=0: 
            while l < m:
                if a[l]<a[r]:
                    l+=1
                else:
                    a[l],a[r]=a[r],a[l]
                    l+=1
            return a
        else:
            r=m
            while l<m:
                if a[l]<a[r]:
                    l+=1
                else:
                    a[l],a[r]=a[r],a[l]
                    r+=1
            return a
#print(mergearray2([1,2,3,0,0,0],3,[-3,-1,7],3))

##def mergearray3(a,m,b,n):
    #l,r=0,m+n-1
    #if n==0: return a
    #elif m==0: return b
    #else:
        #while l <= r:
            #if
def mergearray3(a,m,b,n):
    l,r=0,0
    c=[]
    if n==0: return a
    elif m==0: return b
    else:
        l,r=0,0
        while l<m:
            print(a,l,r)
            if r<n:
                if a[l] < b[r]:
                    l+=1
                else:
                    a[l],a[l+m]=b[r],a[l]
                    r+=1
            else:
                if a[l]!=0:
                    a[l]=a[l]
                    l+=1
                else:
                    l+=1
        if r < n:
            while r < n:
                a[m+r]=b[r]
                r+=1
    return a
print(mergearray3([1,2,3,0,0],3,[-3,-1],2))