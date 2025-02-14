#Crear una función que recibe dos listas ordenadas y te regresa la unión de esas listas ya ordenadas.
def mergesort(l1, l2):
    pointer1 = 0
    pointer2 = 0
    l3 = []
    
    # Mientras ambos punteros no hayan llegado al final de las listas
    while pointer1 < len(l1) and pointer2 < len(l2):
        if l1[pointer1] < l2[pointer2]:
            l3.append(l1[pointer1])
            pointer1 += 1
        else:
            l3.append(l2[pointer2])
            pointer2 += 1
    
    # Si quedan elementos en l1
    while pointer1 < len(l1):
        l3.append(l1[pointer1])
        pointer1 += 1
    
    # Si quedan elementos en l2
    while pointer2 < len(l2):
        l3.append(l2[pointer2])
        pointer2 += 1
    
    return l3
print(mergesort([1,2],[2,3]))