#Given a sorted integer array of N elements. You need to find the maximum sum of two elements such that sum is closest to zero. 

def ClosestSumtoZero(a):
    l,r=0,len(a)-1
    max=0
    min=float('inf')
    while l<r:
        if abs(a[l]+a[r])<min:
            min=abs(a[l]+a[r])
            max=a[l]+a[r]
            l+=1
        else:
            if min==abs(a[l]+a[r]) and a[l]+a[r] > max:
                max=a[l]+a[r]
            r-=1
    return min, max
print(ClosestSumtoZero([-23,-12,-10,43]))
#Se resuelve este código en un tiempo de O(n).