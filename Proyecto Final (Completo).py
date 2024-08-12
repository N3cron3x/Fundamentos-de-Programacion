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

def agregar_evento(eventos):
    while True:
        nombre = input("Nombre del evento: ").strip()
        if not nombre:
            print("El nombre del evento no puede estar vacío. Inténtalo de nuevo.")
            continue
        
        fecha = input("Fecha del evento (dd/mm/aaaa): ")
        if not validar_fecha(fecha):
            print("Fecha inválida. Debe estar en formato dd/mm/aaaa con valores numéricos válidos.")
            continue
        
        hora = input("Hora del evento (hh:mm): ")
        if not validar_hora(hora):
            print("Hora inválida. Debe estar en formato hh:mm con valores numéricos válidos.")
            continue
        
        evento = {'nombre': nombre, 'fecha': fecha, 'hora': hora}
        eventos.append(evento)
        print("Evento agregado correctamente.")
        break

def agregar_tarea(tareas):
    while True:
        descripcion = input("Descripción de la tarea: ").strip()
        if not descripcion:
            print("La descripción de la tarea no puede estar vacía. Inténtalo de nuevo.")
            continue
        
        try:
            prioridad = int(input("Prioridad de la tarea (1-5): "))
            if prioridad < 1 or prioridad > 5:
                raise ValueError
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
        
        tarea = {'descripcion': descripcion, 'prioridad': prioridad, 'fecha': fecha, 'hora': hora}
        tareas.append(tarea)
        print("Tarea agregada correctamente.")
        break

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

def eliminar_evento(eventos):
    while True:
        nombre = input("Nombre del evento a eliminar: ").strip()
        if not nombre:
            print("El nombre del evento no puede estar vacío. Inténtalo de nuevo.")
            continue
        
        for evento in eventos:
            if evento['nombre'] == nombre:
                eventos.remove(evento)
                print(f"Evento '{nombre}' eliminado.")
                return
        print(f"Evento '{nombre}' no encontrado. Inténtalo de nuevo.")

def eliminar_tarea(tareas):
    while True:
        descripcion = input("Descripción de la tarea a eliminar: ").strip()
        if not descripcion:
            print("La descripción de la tarea no puede estar vacía. Inténtalo de nuevo.")
            continue
        
        for tarea in tareas:
            if tarea['descripcion'] == descripcion:
                tareas.remove(tarea)
                print(f"Tarea '{descripcion}' eliminada.")
                return
        print(f"Tarea '{descripcion}' no encontrada. Inténtalo de nuevo.")

eventos = []
tareas = []

while True:
    print("\nAgenda Personal")
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
        agregar_evento(eventos)

    elif opcion == '2':
        agregar_tarea(tareas)

    elif opcion == '3':
        mostrar_agenda(eventos, tareas)

    elif opcion == '4':
        eliminar_evento(eventos)

    elif opcion == '5':
        eliminar_tarea(tareas)

    elif opcion == '6':
        print("Saliendo de la agenda... Hasta luego :(")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo. Asegurate de agregar uno de los valores que se muestran en pantalla.")
