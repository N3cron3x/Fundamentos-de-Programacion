# Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos

numeros = [int(input("Introduce un número: ")) for i in range(10)]
posiciones_mas_3_digitos = [i for i, num in enumerate(numeros) if len(str(abs(num))) > 3]
print(f"Los números con más de 3 dígitos están en las posiciones {posiciones_mas_3_digitos}.")