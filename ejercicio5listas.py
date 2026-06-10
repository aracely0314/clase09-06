numeros=[]

for i in range(8):
    while True:
        try:
            numero=int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")
    numeros.append(numero)
numero_mayor=numeros[0]
numero_menor=numeros[0]
for i in range(len(numeros)):
    if numeros[i]>numero_mayor:
        numero_mayor=numeros[i]
    if numeros[i]<numero_menor:
        numero_menor=numeros[i]
        
print(f"Número mayor: {numero_mayor}")
print(f"Número menor: {numero_menor}")