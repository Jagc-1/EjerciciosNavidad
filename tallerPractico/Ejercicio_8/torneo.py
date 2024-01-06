import os

# Función para obtener el número de puntos a favor del jugador
def register_players():
    players_by_categories = {
        "Novato": {"jugadores": [], "min_edad": 15, "max_edad": 16, "registrados": 0},
        "Intermedio": {"jugadores": [], "min_edad": 17, "max_edad": 20, "registrados": 0},
        "Avanzado": {"jugadores": [], "min_edad": 21, "max_edad": 99, "registrados": 0}
    }

    for category, info in players_by_categories.items():
        os.system('cls')
        print("-----------------------------------------")
        print(f"INSCRIPCION DE LOS JUGADORES PARA LA CATEGORIA {category}:")
        print("------ Registre 5 Jugadores Para Esta Categoria ------")
        print("-----------------------------------------")

        while info["registrados"] < 5:
            name = input("Nombre del jugador o S para finalizar: ").strip()
            if name.lower() == 's':
                break
            try:
                age = int(input("Edad del jugador: "))
                if not (info["min_edad"] <= age <= info["max_edad"]):
                    print(f"Lo siento, el jugador debe tener entre {info['min_edad']} y {info['max_edad']} años para la categoría {category}.")
                    print("----------------------------------------")
                    continue

                player_id = int(input('Ingrese ID: '))
                player = {"nombre": name, "edad": age, "ID": player_id, "PJ": 0, "PG": 0, "PP": 0, "PA": 0, 'TP': 0}
                info["jugadores"].append(player)
                info["registrados"] += 1
                print(f"{name} registrado exitosamente para la categoría {category}.")
                print("----------------------------------------")
            except ValueError:
                print("Ingrese un valor correcto.")
                continue

        if info["registrados"] < 5:
            print("--------------------------------------------------------------------------")
            print(f"No hay suficientes jugadores en la categoría {category} para iniciar el torneo.🏓")
            input("Presiona Enter para continuar...")

    return players_by_categories

# Función para registrar puntos de los jugadores
def register_points(players_by_categories):
    for category, info in players_by_categories.items():
        os.system('cls')
        print(f"\nResultados para la categoría {category}:")
        for player in info["jugadores"]:
            print('-----------------------------------------------------')
            print(f"\nJugador: {player['nombre']}")
            score_player = int(input(f"Puntos para {player['nombre']}: "))

            while True:
                try:
                    score_opponent = int(input(f"Puntos para el contrincante de {player['nombre']}: "))
                    break
                except ValueError:
                    print("Ingrese un valor correcto para el puntaje del contrincante.")

            # Calcular la diferencia de puntos
            score_difference = score_player - score_opponent

            # Actualizar los puntos y partidos jugados para cada jugador
            player["PJ"] += 1

            if score_difference > 0:
                player["PG"] += 1
            elif score_difference < 0:
                player["PP"] += 1

            # Actualizar puntos a favor considerando la diferencia de puntos
            player["PA"] += score_difference

    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if player["PG"] > 0:
                player["TP"] = player["PJ"] * 2
            if player["PA"] < 0:
                player["PA"] = 0


    print("\nRegistro de resultados completado.")
    os.system('pause')
    os.system('cls')


# Función para ver las estadísticas de un jugador
def view_statistics(players_by_categories: dict) -> None:
    name_player = input("Ingrese nombre del jugador: ")
    os.system('pause')

    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if name_player == player["nombre"]:
                os.system('cls')
                print("El jugador está registrado en la categoría:", category)
                print("ID\t\tNombre\t\tPJ\tPG\tPP\tPA\tTP")
                print(f"{player['ID']}\t{player['nombre']}\t{player['PJ']}\t{player['PG']}\t{player['PP']}\t{player['PA']}\t{player['TP']}")
                os.system('pause')
                return

    print("Jugador no encontrado en ninguna categoría.")
    os.system('pause')

# Función para obtener los ganadores de cada categoría
def get_winners(players_by_categories: dict) -> dict:
    ganadores = {}
    for categoria, infoCat in players_by_categories.items():
        if infoCat["jugadores"]:
            ganador = max(infoCat["jugadores"], key=lambda player: player["PA"])
            ganadores[categoria] = {
                "nombre": ganador["nombre"],
                "puntos_a_favor": ganador["PA"]
            }
            print(f"Ganador en la categoría {categoria}: {ganador['nombre']} con {ganador['PA']} puntos a favor.")
        else:
            ganadores[categoria] = None
            print(f"No hay jugadores registrados en la categoría {categoria}.")
    os.system('pause')
    return ganadores
