def bubble(l):
    left=0
    right=1
    sum=0
    while right < len(l):
        if l[left] < l[right]:
            left+=1
            right+=1
        else:
            l[left], l[right] = l[right], l[left]
            sum+=1
            left+=1
            right+=1
    if sum==0:
        return l
    else:
        return(bubble(l))
print(bubble([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))