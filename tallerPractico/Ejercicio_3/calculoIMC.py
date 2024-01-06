import os
estudiantes = []

for i in range(1, 3):
    os.system("clear")  # Cambié "cls" por "clear" para sistemas Unix
    nombre = input(f"Ingrese el nombre del alumno #{i}: ").lower()
    while any(caracter.isdigit() for caracter in nombre):
        print("El nombre no puede contener números")
        nombre = input(f"Ingrese el nombre del alumno #{i}: ").lower()

    try:
        edad = int(input("Ingrese la edad del alumno: "))
        while edad <= 0:
            print("La edad no puede ser negativa ni 0")
            edad = int(input("Ingrese la edad del alumno: "))
    except ValueError:
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    try:
        peso = float(input("Ingrese el peso del alumno en kilogramos (por ejemplo, 70.5): "))
        while peso <= 0:
            print("El peso no puede ser negativo ni 0")
            peso = float(input("Ingrese el peso del alumno en kilogramos (por ejemplo, 70.5): "))
    except ValueError:
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    try:
        altura = float(input("Ingrese la altura del alumno en metros (por ejemplo, 1.75): "))
        while altura <= 0:
            print("La altura no puede ser negativa ni 0")
            altura = float(input("Ingrese la altura del alumno en metros (por ejemplo, 1.75): "))
    except ValueError:
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    est = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "altura": altura
    }

    estudiantes.append(est)
    # Calcula el IMC y determina el estado para cada estudiante
    imc = peso / altura ** 2
    # Inicializa returno con un valor por defecto
    returno = "No se puede determinar"

    if imc > 18.5 and imc < 24.9:
        returno = "Normal"
    elif imc > 25 and imc < 29.9:
        returno = "Sobrepeso"
    elif imc > 30 and imc < 34.9:
        returno = "Obesidad"
    elif imc > 35 and imc < 39.9:
        returno = "Obesidad 2"
    elif imc > 40:
        returno = "Obesidad 3"

    # Imprime la información de cada estudiante
    print(f"\nDetalles del Estudiante #{i}: {est} - Estado: {returno}")

    try:
        rep = input("Desea agregar otro estudiante? S(si) N(no)").upper()
    except ValueError:
        print("Caracter invalido, solo se permiten 'S' o 'N'")
        rep = input("Desea agregar otro estudiante? S(si) N(no)").upper()

    while rep != "S" and rep != "N":
        print("Caracter Invalido!!")
        rep = input("Desea agregar otro estudiante? S(si) N(no)").upper()

    if rep == "N":
        break
