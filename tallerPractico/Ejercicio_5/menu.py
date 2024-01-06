menu = "1. Registrar Ciudad\n2. Registrar Sismos\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir\n"
hasError = True
def menuPrincipal() -> int:
    header = """
    ******************************
    * Bienvenido a la aplicación *
    ******************************
    """
    print(header)
    print(menu)
    global hasError
    hasError = True
    while hasError:
        try:
            hasError = False
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")
            hasError = True

def informe_riesgo(ciudades):
    for ciudad in ciudades:
        codigo = ciudad[0]
        nombre = ciudad[1]
        prom = ciudad[2]
        riesgo = ""
        if prom < 2.5:
            riesgo = "Amarillo (Sin riesgo)"
        elif 2.6 <= prom <= 4.5:
            riesgo = "Naranja (Riesgo medio)"
        else:
            riesgo = "Rojo (Riesgo alto)"

        print(f"Ciudad: {nombre}, Riesgo: {riesgo}")
