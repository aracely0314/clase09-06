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
    if opcion=="1":
        nombre=input("Ingrese el nombre del estudiante: ").strip().title()
        estudiantes.append(nombre)
        print(f"Estudiante '{nombre}' agregado exitosamente.")
        break
    elif opcion=="2":
        nombre=input("Ingrese el nombre del estudiante a buscar: ").strip().title()
        if nombre in estudiantes:
            print(f"Estudiante '{nombre}' encontrado en la lista.")
        else:
            print(f"Estudiante '{nombre}' no encontrado en la lista.")
    elif opcion=="3":
        nombre=input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
        if nombre in estudiantes:
            estudiantes.remove(nombre)
            print(f"Estudiante '{nombre}' eliminado exitosamente.")
        else:
            print(f"Estudiante '{nombre}' no encontrado en la lista.")
            
    elif opcion=="4":
        if not estudiantes:
            print("No hay estudiantes en la lista.")
        else:
            for i in range(len(estudiantes)):
                print(f"Estudiante {i+1}: {estudiantes[i]}")
    elif opcion=="5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    time.sleep(2)