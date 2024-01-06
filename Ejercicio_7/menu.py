import os

menu = "1. Registrar Producto\n2. Visualizar Productos\n3. Actualizar Stock\n4. Informe de Productos Críticos\n5. Cálculo de Ganancia Potencial \n6. Salir\n"

def menuPrincipal() -> int:
    header = """
    ***********************************
    * Sistema de Gestión de Productos *
    ***********************************
    """
    print(header)
    print(menu)
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")
