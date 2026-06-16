# Ejercicio 1: agenda telefónica
def pedir_datos():
    nombre = input("Ingrese nombre: ").strip().title()
    nombre=nombre.replace(" ","")
    if nombre=="":
        print("Error! El nombre no puede estar vacío. Agregue un nombre válido")
    elif not nombre.isalpha():
        print("Error! El nombre debe ser compuesto por letras. Agregue un nombre válido")
    while True:
        try:
            telefono=int(input(f"Ingrese teléfono de {nombre}: "))
            largo=len(str(telefono))
            if largo>1 and largo<10:
                break
            else:
                print("Error! El número de telefono debe tener al menos 9 números")
        except ValueError:
            print("Error! Debe ingresar números enteros")
    return nombre, telefono   

def agregar_datos():
    agenda={}
    for i in range(3):
        nombre, telefono = pedir_datos()
        agenda[nombre]=telefono
    return agenda

def mostrar_agenda(agenda):
    print("Agenda:")
    for k in agenda:
        print(k,"->",agenda[k])

datos=agregar_datos()
mostrar_agenda(datos)

#Ejercicio 1: Alternativa.
def pedir_datos_():
    nombre = input("Ingrese nombre: ").strip().title()
    nombre=nombre.replace(" ","")
    if nombre=="":
        print("Error! El nombre no puede estar vacío. Agregue un nombre válido")
    elif not nombre.isalpha():
        print("Error! El nombre debe ser compuesto por letras. Agregue un nombre válido")
    while True:
        try:
            telefono=int(input(f"Ingrese teléfono de {nombre}: "))
            largo=len(str(telefono))
            if largo>1 and largo<10:
                break
            else:
                print("Error! El número de telefono debe tener al menos 9 números")
        except ValueError:
            print("Error! Debe ingresar números enteros")
    return nombre, telefono

def agregar_datos_():  
    agenda = []       
    for x in range(3):
        nombre, telefono= pedir_datos_()
        contacto = {
            "nombre": nombre,
            "telefono": telefono
        }
        agenda.append(contacto)
    return agenda

def mostrar_agenda_(agenda):
   for contacto in agenda:
        print(contacto["nombre"], "->", contacto["telefono"])
datos_=agregar_datos_()
mostrar_agenda_(datos_)

