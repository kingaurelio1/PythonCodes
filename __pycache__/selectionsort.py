def selection(l,i):
    left=i
    right=i+1
    sum=0
    while right < len(l):
        if l[left] > l[right]:
            left=right
            right +=1
        else:
            right+=1
    if i==len(l)-1:
        return l
    else:
        l[i], l[left]= l[left], l[i]
        i+=1
        return selection(l,i)
print(selection([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0],0))

def selection2(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
    return l

print(selection([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0],0))
