def knapsack(weights, values, capacity, n, memo={}):
    if (n, capacity) in memo:
        return memo[(n, capacity)]  # Si ya se calculó, lo devolvemos

    if n == 0 or capacity == 0:
        return 0  # Si no hay más objetos o capacidad, el valor es 0

    # Si el peso del objeto n es mayor que la capacidad, no lo tomamos
    if weights[n-1] > capacity:
        result = knapsack(weights, values, capacity, n-1, memo)
    else:
        # Elegimos entre no tomarlo o tomarlo (maximizar valor)
        result = max(
            knapsack(weights, values, capacity, n-1, memo),  # No tomar el objeto
            values[n-1] + knapsack(weights, values, capacity - weights[n-1], n-1, memo)  # Tomar el objeto
        )

    memo[(n, capacity)] = result  # Guardamos el resultado en memo
    return result

print(knapsack([1,2,3],[10,20,30],5,3))