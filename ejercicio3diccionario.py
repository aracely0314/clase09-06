# Ejercicio 3: Inventario tienda
inventario = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15
}

print("Inventario")
for k in inventario:
    print(k,"->",inventario[k],"unidades")
while True:
    try:
        producto = input("Ingrese nombre producto: ").strip().title()
        if producto in inventario:
            break
        else:
            print("Error: Producto no encontrado en el inventario.")
    except:
        print("Error al ingresar el producto, ingrese un producto válido de la lista")
        continue
while True:
    try:
        cantidad = int(input("Ingrese cantidad a vender: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número entero para la cantidad.")


if cantidad<=inventario[producto]:
    print("\nVenta realizada")
    inventario[producto] -= cantidad
    print(f"{producto}: {inventario[producto]} unidades")
else:
    print("No existe stock suficiente!")