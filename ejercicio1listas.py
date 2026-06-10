notas=[]
suma=0
for i in range(5):
    while True:
        try:
            nota=int(input("Ingrese la nota del estudiante: "))
            if nota < 1 or nota > 70:
                print("Error: La nota debe estar entre 1 y 70.")
            else: 
                notas.append(nota)
                suma=sum(notas)
                break
        except ValueError:
            print("Error: Por favor, ingrese un número entero para la nota entre 1 y 70.")   

promedio=suma/5

for i in range(len(notas)):
    print(f"Nota {i+1}: {notas[i]}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio:.0f}")