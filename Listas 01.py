# Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
mayor = max(numeros)
posición = numeros.index(mayor) + 1
print(f"El mayor número leído es {mayor} y está en la posición {posición} de la lista.")