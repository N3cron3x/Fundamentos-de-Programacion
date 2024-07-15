# Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista

from math import factorial

numeros = [int(input("Introduce un número: ")) for i in range(10)]
factoriales = [factorial(num) for num in numeros]
print(f"Las factoriales de los números son: {factoriales}")