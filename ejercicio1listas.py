notas=[]

for i in range(5):
    while True:
        try:
            nota=int(input("Ingrese la nota del estudiante: "))
            if nota < 1 or nota > 70:
                print("Error: La nota debe estar entre 1 y 70.")
                continue
            else: 
                notas.append(nota)
        except ValueError:
            print("Error: Por favor, ingrese un número entero para la nota entre 1 y 70.")   


