menu = "1. Registrar nuevo camper\n2. Registro de prueba\n3. Gestor de matricula\n10. Salir\n"

def menuPrincipal() -> int:
    header = """
    ***********************************
    * Registro Campers de Campuslands *
    ***********************************
    """
    print(header)
    print(menu)
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")
