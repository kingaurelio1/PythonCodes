def quick(l):
    if len(l) <=1:
        return l
    else:
        m=len(l)-1
        left=0
        right=m
        pivot=l[right]
        newleft=[]
        newright=[]
        while left < right:
            if l[left] < l[right]:
                newleft.append(l[left])
                left+=1
            else:
                newright.append(l[left])
                left+=1
        return quick(newleft)+[pivot]+quick(newright)
print(quick([1,2,3,4,5,6,0]))