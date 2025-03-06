def sums(a,t):
    left=0
    right=len(a)-1
    while left <= right:
        if a[left]+a[right] < t:
            left+=1
        elif a[left] + a[right] > t:
            right-=1
        else:
            return [left+1,right+1]
    return -1
print(sums([2,3,4],6))