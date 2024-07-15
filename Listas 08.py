# Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.

numeros = [int(input("Introduce un número: ")) for i in range(10)]
negativos = sum(1 for num in numeros if num < 0)
print(f"Hay {negativos} números negativos en la lista.")