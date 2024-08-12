def validar_fecha(fecha):
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    
    dia, mes, año = partes
    if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
        return False
    
    dia, mes, año = int(dia), int(mes), int(año)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1000 <= año <= 9999):
        return False

    return True

def validar_hora(hora):
    partes = hora.split(':')
    if len(partes) != 2:
        return False
    
    horas, minutos = partes
    if not (horas.isdigit() and minutos.isdigit()):
        return False
    
    horas, minutos = int(horas), int(minutos)
    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
        return False

    return True

def agregar_evento(eventos, nombre, fecha, hora):
    if not isinstance(nombre, str) or not validar_fecha(fecha) or not validar_hora(hora):
        return "Datos inválidos. Asegúrate de que el nombre sea una cadena de texto, que la fecha esté en formato dd/mm/aaaa y la hora en hh:mm con valores numéricos."
    
    evento = {'nombre': nombre, 'fecha': fecha, 'hora': hora}
    eventos.append(evento)
    return "Evento agregado correctamente."

def agregar_tarea(tareas, descripcion, prioridad, fecha, hora):
    if not isinstance(descripcion, str) or not isinstance(prioridad, int) or prioridad < 1 or prioridad > 5:
        return "Datos inválidos. Descripción debe ser cadena y prioridad un entero entre 1 y 5."
    if not validar_fecha(fecha) or not validar_hora(hora):
        return "Datos inválidos. Asegúrate de que la fecha esté en formato dd/mm/aaaa y la hora en hh:mm con valores numéricos."
    
    tarea = {'descripcion': descripcion, 'prioridad': prioridad, 'fecha': fecha, 'hora': hora}
    tareas.append(tarea)
    return "Tarea agregada correctamente."

def mostrar_agenda(eventos, tareas):
    print("\n--- Eventos ---")
    if not eventos:
        print("No hay eventos programados.")
    for evento in eventos:
        print(f"Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}")
    
    print("\n--- Tareas ---")
    if not tareas:
        print("No hay tareas programadas.")
    for tarea in tareas:
        print(f"Descripción: {tarea['descripcion']}, Prioridad: {tarea['prioridad']}, Fecha: {tarea['fecha']}, Hora: {tarea['hora']}")

def eliminar_evento(eventos, nombre):
    for evento in eventos:
        if evento['nombre'] == nombre:
            eventos.remove(evento)
            return f"Evento '{nombre}' eliminado."
    return f"Evento '{nombre}' no encontrado."

def eliminar_tarea(tareas, descripcion):
    for tarea in tareas:
        if tarea['descripcion'] == descripcion:
            tareas.remove(tarea)
            return f"Tarea '{descripcion}' eliminada."
    return f"Tarea '{descripcion}' no encontrada."

eventos = []
tareas = []

while True:
    print("\n¡Bienvenido a su agenda personal! :) ")
    print("Aquí están las opciones: ")
    print("--------------------------------------")
    print("1. Agregar Evento")
    print("2. Agregar Tarea")
    print("3. Mostrar Agenda")
    print("4. Eliminar Evento")
    print("5. Eliminar Tarea")
    print("6. Salir")
    print("--------------------------------------")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Nombre del evento: ")
        fecha = input("Fecha del evento (dd/mm/aaaa): ")
        if not validar_fecha(fecha):
            print("Fecha inválida. Debe estar en formato dd/mm/aaaa con valores numéricos válidos.")
            continue
        hora = input("Hora del evento (hh:mm): ")
        if not validar_hora(hora):
            print("Hora inválida. Debe estar en formato hh:mm con valores numéricos válidos.")
            continue
        print(agregar_evento(eventos, nombre, fecha, hora))

    elif opcion == '2':
        descripcion = input("Descripción de la tarea: ")
        try:
            prioridad = int(input("Prioridad de la tarea (1-5): "))
        except ValueError:
            print("Prioridad inválida. Debe ser un número entero entre 1 y 5.")
            continue
        
        fecha = input("Fecha de la tarea (dd/mm/aaaa): ")
        if not validar_fecha(fecha):
            print("Fecha inválida. Debe estar en formato dd/mm/aaaa con valores numéricos válidos.")
            continue
        
        hora = input("Hora de la tarea (hh:mm): ")
        if not validar_hora(hora):
            print("Hora inválida. Debe estar en formato hh:mm con valores numéricos válidos.")
            continue
        
        print(agregar_tarea(tareas, descripcion, prioridad, fecha, hora))

    elif opcion == '3':
        mostrar_agenda(eventos, tareas)

    elif opcion == '4':
        nombre = input("Nombre del evento a eliminar: ")
        print(eliminar_evento(eventos, nombre))

    elif opcion == '5':
        descripcion = input("Descripción de la tarea a eliminar: ")
        print(eliminar_tarea(tareas, descripcion))

    elif opcion == '6':
        print("Saliendo de la agenda... Hasta luego :(")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo. Asegurate de agregar uno de los valores que se muestran en pantalla.")