#Definir una función que dado un array no sorteado de elementos del 1 a n regresa el elemento que se repite y el que falta

def MissingRepeating(l):
    d={}
    sum=0
    sum1=0
    m=(len(l)*(len(l)+1)//2)
    for i in range(len(l)):
        d[l[i]]=i
        sum1+=l[i]
    for j in d.keys():
        sum+=j
    t=m-sum
    sum1+=t
    w=sum1-m
    return t,w
print(MissingRepeating([1,2,4,5,6,7,8,9,7,10]))