# Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista

numeros = [int(input("Introduce un número: ")) for i in range(10)]
promedio_entero = sum(numeros) // len(numeros)
print(f"El promedio entero de los números es {promedio_entero}.")