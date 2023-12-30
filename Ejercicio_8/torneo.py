import os
def points_in_favor(player):
    return player.get("PA",0)

def register_match(player, win, points):
    player["PJ"] += 1
    if win:
        player["PG"] += 2
    else:
        player["PP"] += 1
    player["PA"] += points

def register_player():
    max_players = 12
    total_players = 0

    players_by_categories = {
        "Novato": {"jugadores": [], "min_edad": 15, "max_edad": 16},
        "Intermedio": {"jugadores": [], "min_edad": 17, "max_edad": 20},
        "Avanzado": {"jugadores": [], "min_edad": 21, "max_edad": 99}
    }

    for categorie, info in players_by_categories.items():
        print("-----------------------------------------")
        print(f"INSCRIPCION DE LOS JUGADORES PARA LA CATEGORIA {categorie}:")
        print("------ Registre 5 Jugadores Para Esta Categoria ------")
        print("-----------------------------------------")
        while len(info["jugadores"]) < 5 and total_players < max_players:
            name = input("Nombre del jugador o S para finalizar: ").strip()
            if name.lower() == 's':
                break
            try:
                age = int(input("Edad del jugador: "))
            except ValueError:
                print("Por favor, ingrese una edad válida.")
                continue

            if info["min_edad"] <= age <= info["max_edad"]:
                player = {"nombre": name, "edad": age, "PJ": 0, "PG": 0, "PP": 0, "PA": 0}
                info["jugadores"].append(player)
                total_players += 1
                print(f"{name} registrado exitosamente.")
            else:
                print(f"Lo siento, el jugador debe tener entre {info['min_edad']} y {info['max_edad']} años para la categoría {categorie}.")
                print("----------------------------------------")

        if total_players < 5:
            print("--------------------------------------------------------------------------")
            print(f"No hay suficientes jugadores en la categoría {categorie} para iniciar el torneo.🏓")
            os.system('pause')
            os.system('cls')
            name = input("Nombre del jugador o S para finalizar: ").strip()
            if name.lower() == 's':
                break
            try:
                age = int(input("Edad del jugador: "))
            except ValueError:
                print("Por favor, ingrese una edad válida.")
                continue

            if info["min_edad"] <= age <= info["max_edad"]:
                player = {"nombre": name, "edad": age}
                info["jugadores"].append(player)
                total_players += 1
                print(f"{name} registrado exitosamente.")
                print("----------------------------------------")
            else:
                print(f"Lo siento, el jugador debe tener entre {info['min_edad']} y {info['max_edad']} años para la categoría {categorie}.")

    os.system('cls')
    os.system('pause')
    return players_by_categories

def start_tournament(players_by_categories: dict):
    name_player = input("Ingrese nombre del jugador: ")
    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if name_player == player["nombre"]:
                os.system('cls')
                print("El jugador está registrado en la categoría:", category)
                while True:
                    try:
                        win = input("¿El jugador ganó el partido? (S/N): ").lower()
                        if win in ('s', 'n'):
                            points = int(input("Ingrese la cantidad de puntos a favor del jugador: "))
                            break
                    except ValueError:
                        print("Por favor, ingrese datos válidos.")


                register_match(player, win, points)
                return category
        print("No se encontró el jugador en ninguna categoría.")
    os.system('cls')
    os.system('pause')

def get_winners(torneo: dict) -> dict:
    for categoria, infoCat in torneo.items():
        ganador = max(infoCat["jugadores"], key=points_in_favor)
        print(f"Ganador en la categoría {categoria}: {ganador['nombre']} con {ganador['PA']} puntos a favor.")
