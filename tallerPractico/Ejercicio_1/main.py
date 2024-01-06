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
<<<<<<< HEAD:tallerPractico/Ejercicio_1/main.py
            break
=======
            break 
>>>>>>> 84bb73546cf60bf6a12c29d9c70b974b34f25b69:tallerPractico_I/Ejercicio_1/main.py
        except ValueError:
            print("El número tiene que ser entero")

    while numero < 0:
        print("El número no puede ser negativo")
        while True:
            try:
                numero = int(input(f"Ingrese el {i + 1} número: "))
                print("-----------------")
<<<<<<< HEAD:tallerPractico/Ejercicio_1/main.py
                break
=======
                break 
>>>>>>> 84bb73546cf60bf6a12c29d9c70b974b34f25b69:tallerPractico_I/Ejercicio_1/main.py
            except ValueError:
                print("El número tiene que ser entero")

    numeros.append(numero)

suma_numeros = sum(numeros)
print(f"La suma de los números ingresados es: {suma_numeros}")
