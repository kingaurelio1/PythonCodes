#Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

def RemoveDuplicates(a):
    left=0
    right=1
    d={}
    while right<len(a):
        if a[left] < a[right]:
            d[a[left]]=-1
            left+=1
            right+=1
        else:
            d[a[left]]=-1
            left+=1
            right+=1
    return list(d.keys())
print(RemoveDuplicates([2,2,2,2,2,2,2]))
