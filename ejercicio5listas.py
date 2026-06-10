numeros=[]

for i in range(8):
    while True:
        try:
            numero=int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")
    numeros.append(numero)
