# Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo

numeros = [int(input("Introduce un número: ")) for i in range(10)]
digitos_primos = {2, 3, 5, 7}
cuentan_digito_primo = 0

for num in numeros:
    primer_digito = int(str(abs(num))[0])
    if primer_digito in digitos_primos:
        cuentan_digito_primo += 1

print(f"Hay {cuentan_digito_primo} números que comienzan con un dígito primo.")