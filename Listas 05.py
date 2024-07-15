# Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.

def es_primo(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

def contar_digitos_pares(num):
  return sum(1 for digito in str(abs(num)) if int(digito) % 2 == 0)

numeros = [int(input("Introduce un número: ")) for _ in range(10)]
primos = [num for num in numeros if es_primo(num)]

if primos:
  primo_con_mas_digitos_pares = max(primos, key=contar_digitos_pares)
  posicion_primo = numeros.index(primo_con_mas_digitos_pares)
  print(f"El número primo con más dígitos pares está en la posición {posicion_primo}.")
else:
  print("No hay números primos en la lista.")