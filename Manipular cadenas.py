def main():
    texto = input("Ingrese un texto: ")
    while True:
        print("Elige una opción:")
        print("1.Retornar todo el texto en mayusculas")
        print("2.Retornar todo el texto en minusculas")
        print("3.Retornar los dos primeros caracteres")
        print("4.Retornar los dos ultimos caracteres")
        print("5.Retornar la cantidad de veces que se repite el ultimo caracter")
        print("6.Invertir el texto")
        print("7.Salir")

        mayusculas = texto.upper()
        minusculas = texto.lower()
        retornar_2_primeros_char = texto[:2]
        dos_ultimos_char = texto[-2:]
        ultimo_char = texto[-1]
        repeticiones_ultimo = sum(1 for char in texto if char == ultimo_char)
        invertido = texto[::-1]

        opcion = input("Opción: ")
        if opcion == "1":
            print(mayusculas)
        elif opcion == "2":
            print(minusculas)
        elif opcion == "3":
            print(retornar_2_primeros_char)
        elif opcion == "4":
            print(dos_ultimos_char)
        elif opcion == "5":
            print(repeticiones_ultimo)
        elif opcion == "6": 
            print(invertido)
        elif opcion == '7':
            break
        else:
            print("Opción no válida")
main()
      