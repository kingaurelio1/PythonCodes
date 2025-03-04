def sums(a,t):
    left=0
    right=len(a)-1
    while left < right:
        if a[left]+a[right] < t:
            left+=1
        elif a[left] + a[right] > t:
            right-=1
        else:
            return left,right
    return -1
#Solo funciona si es ordenado.
print(sums([1,2,3,4,5,6,7],12))