dependencias = {}

menu = "1. Registrar Dependencia\n2. Registrar Consumo Por Dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5. Salir\n"

factor_emision = 0.22  # Toneladas de CO2 por MWh
factor_emision_trans = 2.7  # Kilogramos de CO2 por litro de diésel consumido.

def menu_principal() -> int:
    header = """
    *************************
    * Bienvenido al sistema *
    *************************
    """
    print(header)
    print(menu)
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")

        try:
            opcion = int(input("Seleccione la dependencia a registrar: "))
        except ValueError:
                print("Error en el dato ingresado.")
                return

        if opcion in [1, 2, 3]:
            dependencia = {1: 'electricidad', 2: 'transporte', 3: 'dispositivos'}[opcion]
            dependencias[dependencia] = {'consumo': 0}
            print(f"{dependencia.capitalize()} registrada.")
        else:
            print("Opción no válida.")

def registrar_dependencia():
    print("Dependencias:")
    print("1. Electricidad")
    print("2. Transporte")
    print("3. Dispositivos")

    try:
        opcion = int(input("Seleccione la dependencia para registrar consumo: "))
    except ValueError:
        print("Error en el dato ingresado.")
        return

    if opcion in [1, 2, 3]:
        dependencia = {1: 'electricidad', 2: 'transporte', 3: 'dispositivos'}[opcion]

        if dependencia in dependencias:
            if dependencia == 'electricidad':
                consumo_co2 = float(input("Ingrese el consumo de electricidad mensual en CO2: ")) * FACTOR_EMISION
                dependencias[dependencia]['consumo'] += consumo_co2
                print("------------------")

            elif dependencia == 'transporte':
                consumo_km = float(input("Ingrese el consumo de transporte (Kilometros): ")) * FACTOR_EMISION_TRANS
                dependencias[dependencia]['consumo'] += consumo_km
                print("------------------")

            elif dependencia == 'dispositivos':
                potencia = float(input("Ingrese la potencia del dispositivo en vatios (W): "))
                consumo_dispositivos = float(input("Ingrese el tiempo de uso diario del dispositivo en horas: "))
                dependencias[dependencia]['consumo'] += potencia * consumo_dispositivos * 30 / 1000  # Convertir de vatios a kilovatios
                print("------------------")

            print(f"Consumo registrado para {dependencia.capitalize()}.")
        else:
            print("La dependencia no ha sido registrada. ¿Desea registrarla?")
            respuesta = input("Sí(S) / No(N): ").lower()
            if respuesta == 's':
                registrar_dependencia()
    else:
        print("Opción no válida.")

def ver_co2_producido():
    for dependencia, datos in DEPENDENCIAS.items():
        if 'consumo' in datos:
            print(f"{dependencia.capitalize()}: {datos['consumo']} CO2 producido")
        else:
            print(f"{dependencia.capitalize()}: CO2 no registrado")

    input("Presione Enter para continuar...")

def dependencia_mayor_co2():
    if DEPENDENCIAS:
        max_co2 = max(DEPENDENCIAS.keys(), key=lambda x: DEPENDENCIAS[x].get('consumo', 0))
        print(f"La dependencia que produce mayor CO2 es: {max_co2.capitalize()} con {DEPENDENCIAS[max_co2]['consumo']} CO2")
        input("Presione Enter para continuar...")
    else:
        print("No hay dependencias registradas.")
