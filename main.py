# 1. Filtrar elementos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Numeros de la lista:", numeros)
print("Números pares de la lista:", numeros_pares)
print(" ")

# 2. Operaciones matemáticas
lista_numeros = [10, 20, 30, 40, 50]
suma = sum(lista_numeros)
print("Lista de decenas:", lista_numeros)
print("Suma de la lista:", suma)
print(" ")

# 3. Acceder y modificar elementos
frutas = ["manzana", "pera", "uva", "fresa"]
print("Lista de frutas original:", frutas)
print("Primera fruta:", frutas[0]) 
frutas[1] = "banana" 
frutas[2] = "naranja"
print("Lista de frutas actualizada:", frutas)