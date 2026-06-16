# Ejercicio 2: Control de notas
notas = {
    "Pedro": 5.5,
    "María": 6.2,
    "Juan": 4.8,
    "Ana": 7.0
}

nombre = input("Ingrese nombre: ").strip().title()
nombre=nombre.replace(" ","")
if nombre=="":
    print("Error! El nombre no puede estar vacío. Agregue un nombre válido")
elif not nombre.isalpha():
    print("Error! El nombre debe ser compuesto por letras. Agregue un nombre válido")
  
#FORMA 1:
def aprueba1(notas):
    if notas.get(nombre): #se valida que no sea None
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre]>=4:
            return True
        return False
    else:
        print("Alumno no encontrado")
if aprueba1(notas):
    print("Aprueba")
else:
    print("Reprueba")
    
#FORMA 2:
def aprueba2(notas):
    try: #simplemento lo hago, y si falla, no existe
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre]>=4:
            return True
        return False
    except:
            print("Alumno no encontrado")
if aprueba2(notas):
    print("Aprueba")
else:
    print("Reprueba")

#FORMA 3:
def aprueba3(notas):
    if nombre in notas: #ver si existe o no el nombre
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre]>=4:
            return True
        return False
    else:
        print("Alumno no encontrado")
if aprueba3(notas):
    print("Aprueba")
else:
    print("Reprueba")
