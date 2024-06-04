numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))

diferencia = abs(numero1 - numero2)
suma = 0

digito2n1 = numero1 % 10
digito1n1 = numero1//10
digito1n2 = numero2//10
digito2n2 = numero2 % 10

if diferencia % 2 == 0:
    suma = digito1n1+digito1n2+digito2n1+digito2n2
    print("Ya que la diferencia es par, la suma de los digitos de los numeros es: ", suma)
if diferencia == 4 or diferencia % 10 == 4:
    print(f"Los digitos del primer numero son: {digito1n1} y {digito2n1}")
    print(f"Los digitos del primer numero son: {digito1n2} y {digito2n2}")
    print(digito1n1,  digito2n1,  digito1n2,  digito2n2)
if diferencia < 10 and (diferencia == 2 or diferencia == 3 or diferencia == 5 or diferencia == 7):
    print(
        f"La diferencia entre los dos numeros({diferencia}) es un numero primo")
    print("El producto de los numeros es: ", numero1*numero2)
else:
    print("La diferencia no es prima")
    print("La diferencia puede que no sea par, o no es prima, o no termina en 4, o es primo mayor que 10")
