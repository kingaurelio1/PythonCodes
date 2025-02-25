def insertion(l):
    for j in range(1,len(l)):
        key=l[j]
        i=j-1
        while i>=0 and l[i]>key:
            l[i+1]=l[i]
            i-=1
        l[i+1]=key
    return l

print(insertion([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))