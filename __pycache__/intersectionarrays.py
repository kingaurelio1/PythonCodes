def interseccion(a,b):
    d={}
    l=[]
    for i in range(len(a)):
        d[a[i]]=0
    for j in range(len(b)):
        d[b[j]]=1
    for k in range(len(a)):
        d[a[k]]+=1
    for n in d.keys():
        if d[n]==2:
            l.append(n)
    return l
print(interseccion([1,2,3],[2,3,4]))