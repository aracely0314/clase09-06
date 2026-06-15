inventario = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15
}
def mostrar_inventario():
    print("Inventario")
    for k in inventario:
        print(k,"->",inventario[k],"unidades")

def producto_nombre():
    while True:
        try:
            producto=input("Ingrese nombre producto: ").strip().title()
            if producto in inventario:
                return producto
            else:
                print("Error: Producto no encontrado en el inventario.")
        except:
            print("Error al ingresar el producto, ingrese un producto válido de la lista")
            continue

def cantidad_producto():      
    while True:
        try:
            cantidad=int(input("Ingrese cantidad a vender: "))
            if cantidad<0:
                print("Error: La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            return cantidad
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número entero para la cantidad.")

def realizar_venta(inventario, producto,cantidad):
    if cantidad<=inventario[producto]:
        print("\nVenta realizada")
        inventario[producto]-=cantidad
        print(f"{producto}: {inventario[producto]} unidades")
        return
    else:
        print("No existe stock suficiente!")
        return

mostrar_inventario()
producto=producto_nombre()
cantidad=cantidad_producto()
realizar_venta(inventario, producto, cantidad)