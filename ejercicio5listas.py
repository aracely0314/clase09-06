def pedir_numero():
    while True:
        try:
            numero=int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")

def agregar_numeros():
    numeros=[]
    for i in range (8):
        numeros.append(pedir_numero())
    return numeros

def mostrar_resultado(numeros):
    numero_mayor=numeros[0]
    numero_menor=numeros[0]
    for i in range(len(numeros)):
        if numeros[i]>numero_mayor:
            numero_mayor=numeros[i]
        if numeros[i]<numero_menor:
            numero_menor=numeros[i]
    largo=len(numeros)
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    print(f"Cantidad: {largo}")

numeros=agregar_numeros()
mostrar_resultado(numeros)


