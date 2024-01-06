import os
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

dependencias = {}
menu = "1. Registrar Dependencia\n2. Registrar Consumo Por Dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5. Salir\n"
FactorEmision = 0.22  # Toneladas de CO2 por MWh
FactorEmisionTrans = 2.7  # Kilogramos de CO2 por litro de diésel consumido.

def menuPrincipal() -> int:
    print(menu)
    while True:
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato ingresado")

def registrar_dependencia():
    nombre = input("Ingrese el nombre de la dependencia: (electricidad, transporte o dispositivos) ")

    if nombre == 'electricidad':
        dependencias[nombre] = {'consumo': 0}
    elif nombre == 'dispositivos':
        dependencias[nombre] = {'consumo': 0}
    else:
        dependencias[nombre] = {'consumo': 0}

def registrar_consumo():
    dependencia = input("Ingrese el nombre de la dependencia: (electricidad, transporte o dispositivos) ")

    if dependencia in dependencias:
        if dependencia == 'electricidad':
            consumo_co2 = float(input("Ingrese el consumo de electricidad mensual en CO2: ")) * FactorEmision
            dependencias[dependencia]['consumo'] += consumo_co2

        elif dependencia == 'transporte':
            consumo_km = float(input("Ingrese el consumo de transporte (Kilometros): ")) * FactorEmisionTrans
            dependencias[dependencia]['consumo'] += consumo_km



        elif dependencia == 'dispositivos':
            potencia = float(input("Ingrese la potencia del dispositivo en vatios (W): "))
            consumo_dispositivos = float(input("Ingrese el tiempo de uso diario del dispositivo en horas: "))
            dependencias[dependencia]['consumo'] += potencia * consumo_dispositivos * 30 / 1000  # Convertir de vatios a kilovatios
        os.system("pause")

    else:
        print("La dependencia no ha sido registrada.")

def ver_co2_producido():
    for dependencia, datos in dependencias.items():
        if 'consumo' in datos:
            print(f"{dependencia}: {datos['consumo']} CO2 producido")
        else:
            print(f"{dependencia}: CO2 no registrado")
    os.system("pause")

def dependencia_mayor_co2():
    if dependencias:
        max_co2 = max(dependencias.keys(), key=lambda x: dependencias[x].get('consumo', 0))
        print(f"La dependencia que produce mayor CO2 es: {max_co2} con {dependencias[max_co2]['consumo']} CO2")
        os.system("pause")
    else:
        print("No hay dependencias registradas.")
