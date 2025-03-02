#Find the union of two arrays

def Union(a,b):
    d={}
    l=[]
    for i in range(len(a)):
        d[a[i]]=0
    for j in range(len(b)):
        d[b[j]]=1
    return list(d.keys())
print(Union([1,2,3,4,5],[1,2,3,4,6,7,10]))