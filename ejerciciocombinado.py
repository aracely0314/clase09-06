import os, time
estudiantes = {}

menu="""1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Mostrar promedio de un estudiante
5. Mostrar todos los promedios
6. Salir"""

while True:
    os.system("cls")
    print(menu)
    opcion = input("Seleccione una opción: ")
    os.system("cls")
    if opcion == "1":
        print("Agregar estudiante")
        nombre = input("Ingrese el nombre del estudiante: ").strip().title()
        if nombre == "":
            print("El nombre no puede estar vacío.")
        elif nombre in estudiantes:
            print(f"El estudiante {nombre} ya existe.")
        else:
            estudiantes[nombre] = [] 
            print(f"Estudiante {nombre} agregado con éxito.")
        print("Volviendo al menú principal...")
        time.sleep(2)
        continue
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
    time.sleep(2)
