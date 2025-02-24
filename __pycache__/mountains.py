def mountains(l):
    max=0
    left=0
    right=1
    while right < len(l):
        if l[left] < l[right] and right==len(l)-1:
            max=l[right]
            break
        elif l[left] < l[right]:
            left+=1
            right+=1
        else:
            max=l[left]
            break
    return max
print(mountains([1,2,3,4,5,6,7,8,1,23,45,6]))