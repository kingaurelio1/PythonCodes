def sums(a,t):
    left=0
    right=len(a)-1
    while left <= right:
        if a[left]+a[right] < t:
            left+=1
        elif a[left] + a[right] > t:
            right-=1
        else:
            return left,right
    return -1
#Solo funciona si es ordenado.
def sums1(a,t):
    d={}
    for i in range(len(a)):
        d[a[i]]=i
    for j in range(len(a)):
        if t-a[j] in d:
            return d[t-a[j]],j
    return -1
print(sums1([5,6,7,9,5,4,2,9,3,2,4,10,20,6],13))