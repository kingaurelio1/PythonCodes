#Función que rota un array
#Primera solución
def rotatearray(l,n):
    m=len(l)
    k=n%m
    d={}
    if len(l)==1 or k==0 :
        return l
    else:
        for i in range(len(l)):
            d[i]=l[(len(l)-k+i)%(m)]
        r=list(d.values())
    return r
print(rotatearray([1,2,3,4,5,6,7],6))