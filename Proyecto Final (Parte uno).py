eventos = {} 
contador_eventos = 0  
horas_por_dia = 24.0  

def agregar_evento(fecha_str, hora_str, descripcion):
    global contador_eventos
    fecha = fecha_str
    hora = hora_str
    contador_eventos += 1
    id_evento = contador_eventos
    evento = (hora, descripcion)  
    if fecha not in eventos:
        eventos[fecha] = set()  
    eventos[fecha].add((id_evento, evento))
    print("Evento '{}' añadido el {} a las {}.".format(descripcion, fecha, hora))

def actualizar_evento(id_evento, fecha_str, hora_str, nueva_descripcion):
    fecha = fecha_str
    hora = hora_str
    encontrado = False
    for f, evs in eventos.items():
        for e in evs:
            if e[0] == id_evento:
                evs.remove(e)
                evs.add((id_evento, (hora, nueva_descripcion)))
                encontrado = True
                print("Evento {} actualizado a '{}' el {} a las {}.".format(id_evento, nueva_descripcion, fecha, hora))
                break
        if encontrado:
            break
    if not encontrado:
        print("No se encontró el evento con ID {}.".format(id_evento))

def eliminar_evento(id_evento):
    encontrado = False
    for f, evs in eventos.items():
        for e in evs:
            if e[0] == id_evento:
                evs.remove(e)
                encontrado = True
                print("Evento {} eliminado.".format(id_evento))
                break
        if encontrado:
            break
    if not encontrado:
        print("No se encontró el evento con ID {}.".format(id_evento))

def ver_eventos(fecha_str):
    fecha = fecha_str
    if fecha in eventos:
        print("Eventos para el {}:".format(fecha))
        for id_evento, evento in sorted(eventos[fecha]):
            hora, descripcion = evento
            print("ID: {} - {} - {}".format(id_evento, hora, descripcion))
    else:
        print("No hay eventos para el {}.".format(fecha))

def principal():
    while True:
        print("\n¡Bienvenido a su agenda personal! :)")
        print("\nPor favor, elige una de las opciones:")
        print("----------------------------------------")
        print("1. Agregar evento")
        print("2. Actualizar evento")
        print("3. Eliminar evento")
        print("4. Ver eventos por fecha")
        print("5. Salir")
        print("----------------------------------------")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            fecha_str = input("Ingresa la fecha del evento (YYYY-MM-DD): ")
            hora_str = input("Ingresa la hora del evento (HH:MM): ")
            descripcion = input("Ingresa la descripción del evento: ")
            agregar_evento(fecha_str, hora_str, descripcion)
        elif opcion == 2:
            id_evento = int(input("Ingresa el ID del evento a actualizar: "))
            fecha_str = input("Ingresa la nueva fecha del evento (YYYY-MM-DD): ")
            hora_str = input("Ingresa la nueva hora del evento (HH:MM): ")
            nueva_descripcion = input("Ingresa la nueva descripción del evento: ")
            actualizar_evento(id_evento, fecha_str, hora_str, nueva_descripcion)
        elif opcion == 3:
            id_evento = int(input("Ingresa el ID del evento a eliminar: "))
            eliminar_evento(id_evento)
        elif opcion == 4:
            fecha_str = input("Ingresa la fecha para ver eventos (YYYY-MM-DD): ")
            ver_eventos(fecha_str)
        elif opcion == 5:
            print("Esta bien :c. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    principal()