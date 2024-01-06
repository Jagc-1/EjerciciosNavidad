header = """ Bienvenido """
print("-----------------")
print(header)
print("-----------------")

numeros = []
for i in range(3):
    while True:
        try:
            numero = int(input(f"Ingrese el {i + 1} número: "))
            print("-----------------")
            break
        except ValueError:
            print("El número tiene que ser entero")

    while numero < 0:
        print("El número no puede ser negativo")
        while True:
            try:
                numero = int(input(f"Ingrese el {i + 1} número: "))
                print("-----------------")
                break
            except ValueError:
                print("El número tiene que ser entero")

    numeros.append(numero)

suma_numeros = sum(numeros)
print(f"La suma de los números ingresados es: {suma_numeros}")
