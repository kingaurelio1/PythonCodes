def mergesort(l):
    if len(l) <= 1:
        return l
    else:
        middle = len(l) // 2
        left = l[:middle]
        right = l[middle:]
        return merge(mergesort(left), mergesort(right))

def merge(a, b):
    resultado = []
    leftind = 0
    rightind = 0
    
    # Combina ambos arreglos comparando los elementos
    while leftind < len(a) and rightind < len(b):
        if a[leftind] < b[rightind]:
            resultado.append(a[leftind])
            leftind += 1
        else:
            resultado.append(b[rightind])
            rightind += 1

    # Agrega los elementos restantes de la lista a o b
    resultado.extend(a[leftind:])
    resultado.extend(b[rightind:])
    
    return resultado
print(mergesort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))