
def fibonacci_tab(n):
    i=0
    i+=1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Inicializamos los dos primeros valores de la secuencia
    prev2, prev1 = 0, 1

    # Calculamos la secuencia desde 2 hasta n
    for i in range(2, n + 1):
        current = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
        prev2 = prev1  # Actualizamos prev2 para la siguiente iteración
        prev1 = current  # Actualizamos prev1

    return prev1



print(fibonacci_tab(16))

def fibo(n):
    if n<2:
        return n
    else:
        left=0
        right=1
        current=0
        for i in range(2,n):
            current=left+right
            left=right
            right=current
        return right
print(fibo(4))