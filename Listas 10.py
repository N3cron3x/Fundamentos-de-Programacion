# Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
lista_numeros = []
for i in range(10):
    lista_numeros.append(int(input("Ingrese un número: ")))

numero = int(input("Ingrese otro número: "))

contador_divisores = 0
for n in lista_numeros:
    if numero % n == 0:
        contador_divisores += 1

print("El número", numero, "tiene", contador_divisores, "divisores exactos entre los valores en la lista.")