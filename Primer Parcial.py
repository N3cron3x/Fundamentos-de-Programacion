#Calcular el promedio de notas de un estudiante

estudiantes = ['Ingrese el nombre del estudiante: ']

while True:
    nombre_estudiante = input("Ingrese su nombre: ")
    matricula = input("Ingrese su matrícula estudiantil: ")

    while True:
        try:
            nota_1 = int(input("Ingrese la nota 1: "))
            nota_2 = int(input("Ingrese la nota 2: "))
            nota_3 = int(input("Ingrese la nota 3: "))
            nota_4 = int(input("Ingrese la nota 4: "))
            if nota_1 < 0 or nota_2 < 0 or nota_3 < 0 or nota_4 < 0:
                print("Las notas no pueden ser negativas. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Las calificaciones deben ser números enteros. Inténtelo de nuevo.")

    resultado = (nota_1 + nota_2 + nota_3 + nota_4) / 4

    if resultado <= 69:
        print(f"El estudiante {nombre_estudiante} sacó {resultado} y reprobó")
    elif 70 <= resultado <= 100:
        print(f"El estudiante {nombre_estudiante} sacó {resultado} y aprobó")

    estudiantes.append((nombre_estudiante, resultado))

    continuar = input("¿Quiere capturar otro estudiante? (si/no): ").lower()
    if continuar != 'si':
        break

print("\nPromedios de los estudiantes capturados:")
for estudiante, promedio in estudiantes:
    print(f"{estudiante}: {promedio}")
