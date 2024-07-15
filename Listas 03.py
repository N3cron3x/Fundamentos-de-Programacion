# Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído. Escribelo en python, sin usar una funcion y en español

numeros = []
for i in range(10):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

mayor_primo = 0
posicion_mayor_primo = 0

for i in range(len(numeros)):
    es_primo = True
    for j in range(2, int(numeros[i]**0.5) + 1):
        if numeros[i] % j == 0:
            es_primo = False
            break
    if es_primo and numeros[i] > mayor_primo:
        mayor_primo = numeros[i]
        posicion_mayor_primo = i

print("El mayor número primo es", mayor_primo, "y está en la posición", posicion_mayor_primo)