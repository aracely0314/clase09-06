def pedir_numero(numero):
    while True:
        try:
            numero=int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero")

def agregar_numeros():
    numeros = []
    for i in range(5):
        numeros.append(pedir_numero())
    return numeros

def sumar(numeros):
    suma=sum(numeros)
    return suma

def promediar(numeros):
    promedio=suma / len(numeros)
    return promedio

def mostrar_resultados(numeros, suma, promedio):
    for i, numero in enumerate(numeros,1):
        print(f"Número {i}: {numero}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.0f}")

numeros=agregar_numeros()
suma=sumar(numeros)
promedio=promediar(numeros)
mostrar_resultados(numeros, suma, promedio)


