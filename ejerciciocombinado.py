import os, time
estudiantes={}
menu="""1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Mostrar promedio de un estudiante
5. Mostrar todos los promedios
6. Salir"""

def mostrar_menu():
    os.system("cls")
    print(menu)

def agregar_estudiante():
    while True:
        print("Agregar estudiante")
        nombre=input("Ingrese el nombre del estudiante: ").strip().title()
        nombre_sin_espacios = nombre.replace(" ", "")
        if nombre=="":
            print("Error! El nombre no puede estar vacío. Agregue un nombre válido")
            continue
        elif nombre in estudiantes:
            print(f"El estudiante {nombre} ya existe. Agregue un nombre válido")
            continue
        elif not nombre_sin_espacios.isalpha():
            print("Error! El nombre debe ser compuesto por letras. Agregue un nombre válido")
            continue
        else:
            estudiantes[nombre]=[] 
            print(f"Estudiante {nombre} agregado con éxito.")
            print("Volviendo al menú principal...")
            break

def agregar_nota():
    if len(estudiantes)==0:
        print("No hay estudiantes para agregar notas")
    else:
        print("Agregar nota")
        nombre= input("Ingrese el nombre del estudiante al que desea agregar una nota: ").strip().title()
        if nombre not in estudiantes:
            print(f"El estudiante {nombre} no existe.")
        else:
            while True: 
                try:
                    nota=float(input("Ingrese la nota del estudiante: "))
                    if nota>=1.0 and nota<=7.0:
                        estudiantes[nombre].append(nota)
                        print(f"Nota agregada con éxito al estudiante {nombre}.")
                        print("Volviendo al menú...")
                        break
                    else:
                        print("Error! La nota debe ser entre '1.0' y '7.0'.")
                except ValueError:
                    print("Error! Por favor, ingrese un número decimal válido.")

def mostrar_estudiantes():
    if len(estudiantes)==0:
        print("No hay estudiantes en la lista.")
        time.sleep(1)
    else:
        print("Mostrar estudiantes")
        for i, nombre in enumerate(estudiantes,1):
            print(f"Estudiante {i}: {nombre}")
        time.sleep(3)

def mostrar_promedio():
    if len(estudiantes)==0:
        print("No hay estudiantes en la lista.")
    else:
        print("Mostrar promedio de un estudiante")
        nombre= input("Ingrese el nombre del estudiante para mostrar su promedio: ").strip().title()
        if nombre not in estudiantes:
            print(f"El estudiante {nombre} no existe en la lista.")       
        else:
            if len(estudiantes[nombre])==0:
                print(f"El estudiante {nombre} no tiene notas registradas.")
            else:
                notas=estudiantes[nombre]
                suma=sum(notas)
                promedio=suma/len(notas)
                print(f"El promedio del estudiante {nombre} es: {promedio:.1f}")

def mostrar_todos_promedios():
    if len(estudiantes)==0:
        print("No hay estudiantes en la lista para promediar.")
    else:
        print("Mostrar todos los promedios")
        for nombre in estudiantes.keys():
            notas=estudiantes[nombre] 
            if len(notas)>0:
                suma=sum(notas)
                promedio=suma/len(notas)
                print(f"{nombre} -> {promedio:.1f}")
            else:
                print(f"{nombre} -> no tiene notas registradas para promediar")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion=input("Seleccione una opción: ")
        os.system("cls")
        if opcion=="1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_nota()
        elif opcion == "3":
            mostrar_estudiantes()
        elif opcion == "4":
            mostrar_promedio()
        elif opcion == "5":
            mostrar_todos_promedios()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        time.sleep(2)
ejecutar_menu()
