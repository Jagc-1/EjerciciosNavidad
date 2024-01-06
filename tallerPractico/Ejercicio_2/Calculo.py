import os
estudiantes = []

for i in range(1, 3):
    os.system("cls")
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
        os.system("cls")
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    try:
        peso = float(input("Ingrese el peso del alumno en kg: "))
        while peso <= 0:
            print("El peso no puede ser negativo ni 0")
            peso = float(input("Ingrese el peso del alumno en kg: "))
    except ValueError:
        os.system("cls")
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    try:
        altura = float(input("Ingrese la altura del alumno en metros: "))
        while altura <= 0:
            print("La altura no puede ser negativa ni 0")
            altura = float(input("Ingrese la altura del alumno en metros: "))
    except ValueError:
        os.system("cls")
        print("Carácter inválido, solo se permiten valores numéricos")
        continue

    est = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "altura": altura
    }

    estudiantes.append(est)

    imc = peso / altura ** 2

if imc > 18.5 and imc < 24.9:
    returno= "Normal"
elif imc > 25 and imc < 29.9:
    returno = "Sobrepeso"
elif imc > 30 and imc < 34.9:
    returno = "Obesidad"
elif imc > 35 and imc < 39.9:
    returno = "Obesidad 2"
elif imc > 40:
    returno = "Obesidad 3"

# Imprime la información de todos los estudiantes
print("\nDetalles de todos los estudiantes:")
for idx, estudiante in enumerate(estudiantes, start=1):
    print(f"\nEstudiante #{idx}:")
    for key, value in estudiante.items():
        print(f"{key}: {value}")

# Pregunta al usuario si desea agregar más estudiantes
rep = input("¿Desea agregar más estudiantes? S(si) N(no)").upper()
while rep != "S" and rep != "N":
    print("Caracter Invalido!!")
    rep = input("¿Desea agregar más estudiantes? S(si) N(no)").upper()

if rep == "S":
    isActive = True
else:
    isActive = False
