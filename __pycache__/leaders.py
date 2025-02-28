#Leaders

def Leaders(l):
    right=len(l)-1
    left=right-1
    m=[l[-1]]
    max1=l[-1]
    while right > 0:
        print(m,left,right,max1)
        if max1 < l[left]:
            max1=max(max1,l[left])
            m=[max1]+m
            left-=1
            right-=1
        else:
            left-=1
            right-=1
    return m
print(Leaders([16, 17, 4, 3, 5, 2]))

