def binarysearch(l, n, low=0, high=None):
    if high is None:
        high = len(l) - 1
    
    # Caso base: si el rango es inválido, el número no está en la lista
    if low > high:
        return False
    
    middle = (low + high) // 2

    # Si encontramos el número en el medio, lo devolvemos
    if l[middle] == n:
        return True
    # Si el número es mayor que el del medio, lo buscamos en la mitad derecha
    elif n > l[middle]:
        return binarysearch(l, n, middle + 1, high)
    # Si el número es menor que el del medio, lo buscamos en la mitad izquierda
    else:
        return binarysearch(l, n, low, middle - 1)

    
print(binarysearch([1,2,3,4],5))