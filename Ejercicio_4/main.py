import os

total_numeros = 0
total_pares = 0
suma_pares = 0
suma_impares = 0
menores_10 = 0
entre_20_y_50 = 0
mayores_100 = 0

while True:
    try:
        numero = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))
        if numero < 0:
            break

        total_numeros += 1

        if numero % 2 == 0:
            total_pares += 1
            suma_pares += numero
        else:
            suma_impares += numero

        if numero < 10:
            menores_10 += 1
        elif 20 <= numero <= 50:
            entre_20_y_50 += 1
        elif numero > 100:
            mayores_100 += 1

    except ValueError:
        print("Solo se puede ingresar números enteros.")

if total_numeros > 0:
    if total_pares > 0:
        promedio_pares = suma_pares / total_pares
    else:
        promedio_pares = 0

    if (total_numeros - total_pares) > 0:
        promedio_impares = suma_impares / (total_numeros - total_pares)
    else:
        promedio_impares = 0

    os.system('cls')
    print("-----------------------------------------------------")
    print("Total de números ingresados:", total_numeros)
    print("Total de números pares:", total_pares)
    print("Promedio de los números pares:", promedio_pares)
    print("Promedio de los números impares:", promedio_impares)
    print("Cantidad de números menores que 10:", menores_10)
    print("Cantidad de números entre 20 y 50:", entre_20_y_50)
    print("Cantidad de números mayores que 100:", mayores_100)
    print("-----------------------------------------------------")
else:
    print("No se ingresaron números.")
