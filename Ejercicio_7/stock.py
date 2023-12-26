import os
productos = []

def validacion(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def registrar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    vCompra = validacion("Ingrese el valor de compra del producto: ")
    vVenta = validacion("Ingrese el valor de venta del producto: ")
    stockMin = int(input("Ingrese el stock mínimo permitido (UDS minimas): "))
    stockMax = int(input("Ingrese el stock máximo permitido (UDS maximas): "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")

    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'valor_compra': vCompra,
        'valor_venta': vVenta,
        'stock_minimo': stockMin,
        'stock_maximo': stockMax,
        'proveedor': proveedor,
        'stock': 0
    }

    productos.append(producto)

def visualizar_productos():
    print("\nLista de Productos:")
    for producto in productos:
        print(f"Código: {producto['codigo']}\nNombre: {producto['nombre']}\n"
              f"Valor de Compra: ${producto['valor_compra']:.3f}\n"
              f"Valor de Venta: ${producto['valor_venta']:.3f}\n"
              f"Stock Actual: {producto['stock']}")
    os.system("pause")

def actualizar_stock():
    codProducto = input("Ingrese el código del producto: ").strip()
    cantidad = int(input("Ingrese la cantidad que desea agregar: "))

    for producto in productos:
        if producto['codigo'] == codProducto:
            producto['stock'] += cantidad
            print("Stock actualizado con éxito!")
            break
    else:
        print("Error: Producto no encontrado.")
        print("Lista de productos:")
        for producto in productos:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Stock: {producto['stock']}")
    os.system("pause")
def informe_productos_criticos():
    print("\nProductos Críticos:")
    for producto in productos:
        if producto['stock'] < producto['stock_minimo']:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Stock Actual: {producto['stock']}")
    os.system("pause")

def calcular_ganancia_potencial():
    totalGanancia = 0

    for producto in productos:
        gananciaProducto = (producto['valor_venta'] - producto['valor_compra']) * producto['stock']
        totalGanancia += gananciaProducto

    print(f"\nGanancia Potencial Total: ${totalGanancia}")
    os.system("pause")
