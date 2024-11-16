# 1. Calcular el factorial de un número (n)
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# 2. Generar los primeros n números de la serie Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    serie = [0, 1]
    for _ in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie

# 3. Sumar los elementos de un arreglo
def suma_arreglo(arr):
    return sum(arr)

# 4. Realizar una multiplicación a base de sumas
def multiplicacion_por_sumas(a, b):
    resultado = 0
    for _ in range(abs(b)):
        resultado += abs(a)
    # Ajustar el signo para el resultado final si alguno de los valores es negativo
    return resultado if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -resultado

# 5. Realizar una división a base de restas
def division_por_restas(dividendo, divisor):
    if divisor == 0:
        raise ValueError("La división por cero no está definida.")
    cociente = 0
    dividendo_absoluto = abs(dividendo)
    divisor_absoluto = abs(divisor)
    
    while dividendo_absoluto >= divisor_absoluto:
        dividendo_absoluto -= divisor_absoluto
        cociente += 1
    
    # Ajustar el signo del resultado final
    return cociente if (dividendo >= 0 and divisor > 0) or (dividendo < 0 and divisor < 0) else -cociente
