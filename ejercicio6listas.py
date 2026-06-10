import os, time
estudiantes=[]
menu="""1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Mostrar estudiantes
5. Salir"""

while True:
    os.system("cls")
    print(menu)
    opcion=input("Seleccione una opción: ")
    os.system("cls")
    if opcion=="1":
        print("Agregar estudiante")
        nombre=input("Ingrese el nombre del estudiante: ").strip().title()
        estudiantes.append(nombre)
        print(f"Estudiante '{nombre}' agregado exitosamente.")
        print("Volviendo al menú principal...")
    elif opcion=="2":
        print("Buscar estudiante")
        buscar=input("Ingrese el nombre del estudiante a buscar: ").strip().title()
        for i in range(len(estudiantes)):
            if estudiantes[i] == buscar:
                print(f"Estudiante '{buscar}' encontrado en la lista en la posición {i+1}.")
                print("Volviendo al menú principal...")
                break
        if buscar not in estudiantes:
            print(f"Estudiante '{buscar}' no encontrado en la lista.")
            print("Volviendo al menú principal...")
    elif opcion=="3":
        print("Eliminar estudiante")
        eliminar=input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
            print(f"Estudiante '{eliminar}' eliminado exitosamente.")
            print("Volviendo al menú principal...")
        else:
            print(f"Estudiante '{eliminar}' no encontrado en la lista.")
            print("Volviendo al menú principal...")
    elif opcion=="4":
        print("Mostrar estudiantes")
        if not estudiantes:
            print("No hay estudiantes en la lista.")
            print("Volviendo al menú principal...")
        else:
            for i in range(len(estudiantes)):
                print(f"Estudiante {i+1}: {estudiantes[i]}")
            print("Volviendo al menú principal...")
    elif opcion=="5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    time.sleep(2)