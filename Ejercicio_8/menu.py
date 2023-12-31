import os
menu = "1. Registrar Jugador\n2. Registrar puntos\n3. Ver ganadores\n4. Salir\n"

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
