import os
menu = "1. Registrar Jugador\n2. Registrar puntos\n3. Ver estadisticas\n4. Ver ganadores\n5. Salir\n"

def menuPrincipal() -> int:

    header = """
    ***********************************
    * Bienvenidos Al Torneo De Tenis *
    ***********************************
    """
    print(header)
    print(menu)
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")
