#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def stairs(n):
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
    