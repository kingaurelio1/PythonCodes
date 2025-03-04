def Tribonacci(n):
    i=0
    i+=1
    if n == 0:
        return 0
    elif n == 1 or n==2:
        return 1

    # Inicializamos los dos primeros valores de la secuencia
    prev3, prev2, prev1 = 0, 1, 1

    # Calculamos la secuencia desde 2 hasta n
    for i in range(2,n):
        current = prev1 + prev2 + prev3 
        prev3 = prev2
        prev2=prev1
        prev1 = current  # Actualizamos prev1

    return prev1

print(Tribonacci(25))