# Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.

numeros = [int(input("Introduce un número: ")) for i in range(10)]
pares = [num for num in numeros if num % 2 == 0]
if pares:
    maximo_par = max(pares)
    posicion_maximo_par = numeros.index(maximo_par)
    print(f"El mayor número par está en la posición {posicion_maximo_par}.")
else:
    print("No hay números pares en la lista.")