def calcular_factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        return "El número debe ser no negativo."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Pedir al usuario un número
try:
    numero = int(input("Ingresa un número entero no negativo: "))
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
