def RemoveEle(a,k):
    left=0
    count=0
    while left < len(a):
        if a[left]==k:
            count+=1
            left+=1
        else:
            left+=1
    return len(a)-count
print(RemoveEle([0,1,2,2,3,0,4,2],2))