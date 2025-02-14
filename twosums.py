#Crear una función que recibe dos entradas una lista y un entero. Regresa los índices de los enteros en la lista que al sumar dan el resultado.
def twosums(l,target):
    left=0
    right=len(l)-1
    n1=0
    n2=0
    while left <= right:
        if l[left] + l[right] < target:
            left +=1
        elif l[left] + l[right] > target:
            right-=1
        else:
            n1=left
            n2=right
            break
    return n1,n2,l[n1],l[n2]
print(twosums([1,2,3,4,5,6,7,8,9],4))