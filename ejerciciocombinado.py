import os, time
estudiantes = {}
suma=0
cantidad_notas=0
menu="""1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Mostrar promedio de un estudiante
5. Mostrar todos los promedios
6. Salir"""

while True:
    os.system("cls")
    print(estudiantes)#borrar esta línea después de probar el programa
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
        time.sleep(1)
        continue
    elif opcion == "2":
        print("Agregar nota")
        nombre= input("Ingrese el nombre del estudiante al que desea agregar una nota: ").strip().title()
        if nombre not in estudiantes:
            print(f"El estudiante {nombre} no existe.")
            time.sleep(2)
            continue
        else:
            while True: 
                try:
                    nota=int(input("Ingrese la nota del estudiante: "))
                    if nota>=1 and nota<=70:
                        for i in range(len(estudiantes)):
                            if nombre in estudiantes:
                                estudiantes[nombre].append(nota)
                                break
                        print(f"Nota agregada con éxito al estudiante {nombre}.")
                        break
                    else:
                        print("La nota debe estar entre 1 y 70.")
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")
    elif opcion == "3":
        print("Mostrar estudiantes")
        if len(estudiantes) == 0:
            print("No hay estudiantes en la lista.")
            time.sleep(1)
        else:
            for k in range(len(estudiantes)):
                print(f"Estudiante {k+1}: {list(estudiantes.keys())[k]}")
            time.sleep(3)
    elif opcion == "4":
        if len(estudiantes) == 0:
            print("No hay estudiantes en la lista.")
            time.sleep(1)
            continue
        print("Mostrar promedio de un estudiante")
        nombre= input("Ingrese el nombre del estudiante para mostrar su promedio: ").strip().title()
        if nombre not in estudiantes:
            print(f"El estudiante {nombre} no existe.")
            time.sleep(1)
            continue
        else:
            if len(estudiantes[nombre]) == 0:
                print(f"El estudiante {nombre} no tiene notas registradas.")
                time.sleep(2)
                continue
            else:
                notas = estudiantes[nombre]
                if len(notas)>0:
                    suma=0
                    cantidad_notas=0
                    for nota in notas:
                      suma+=nota
                      cantidad_notas+=1
                    promedio=suma/cantidad_notas
                    print(f"El promedio del estudiante {nombre} es: {promedio:.1f}")
                else:
                    print(f"El estudiante {nombre} no tiene notas registradas.")
                time.sleep(2)
    elif opcion == "5":
        print("Mostrar todos los promedios")
        if len(estudiantes) == 0:
            print("No hay estudiantes en la lista para promediar.")
            time.sleep(1)
            continue
        for nombre in estudiantes.keys():
            notas=estudiantes[nombre] 
            if len(notas)>0:
                suma=0
                cantidad_notas=0
                for nota in notas:
                    suma+=nota
                    cantidad_notas+=1
                    promedio=suma/cantidad_notas
                print(f"El promedio del estudiante {nombre} es: {promedio:.1f}")
            else:
                print(f"El estudiante {nombre} no tiene notas registradas.")
                time.sleep(3)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
    time.sleep(1)
