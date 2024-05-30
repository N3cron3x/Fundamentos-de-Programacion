def contar_vocales():
    palabra = input("Ingrese la palabra: ")
    vocales = ["a", "e", "i", "o", "u"]
    contador = [0, 0, 0, 0, 0]

    for char in palabra:
        if char.lower() in vocales:
            indice = vocales.index(char.lower())
            contador[indice] += 1

    total = 0
    for count in contador:
        total += count
    print(f"Vocales totales: {total}")

    respuesta = input("¿Desea intentar de nuevo? (s/n): ")
    if respuesta.lower() == "s":
        contar_vocales()
    else:
        print("tt")

contar_vocales()