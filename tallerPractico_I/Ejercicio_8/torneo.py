import os
#Function to obtain the number of points in favor of the player
def points_in_favor(player):
    return player.get("PA")

#Function por registrer  the player
def register_player():
    players_by_categories = {
        "Novato": {"jugadores": [], "min_edad": 15, "max_edad": 16, "registrados": 0},
        "Intermedio": {"jugadores": [], "min_edad": 17, "max_edad": 20, "registrados": 0},
        "Avanzado": {"jugadores": [], "min_edad": 21, "max_edad": 99, "registrados": 0}
    }

    for category, info in players_by_categories.items():
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
                player_id = int(input('Ingrese ID: '))
            except ValueError:
                print("Ingrese un valor correcto.")
                continue

            if info["min_edad"] <= age <= info["max_edad"]:
                player = {"nombre": name, "edad": age, "ID": player_id, "PJ": 0, "PG": 0, "PP": 0, "PA": 0, 'TP': 0}
                info["jugadores"].append(player)
                info["registrados"] += 1
                print(f"{name} registrado exitosamente para la categoría {category}.")
                print("----------------------------------------")
            else:
                print(f"Lo siento, el jugador debe tener entre {info['min_edad']} y {info['max_edad']} años para la categoría {category}.")
                print("----------------------------------------")

        if info["registrados"] < 5:
            print("--------------------------------------------------------------------------")
            print(f"No hay suficientes jugadores en la categoría {category} para iniciar el torneo.🏓")
            input("Presiona Enter para continuar...")
    os.system('cls')
    return players_by_categories

#Function por registrer points of the player
def registrer_points(players_by_categories: dict) -> dict:
    name_player = input("Ingrese nombre del jugador: ")
    os.system('pause')

    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if name_player == player["nombre"]:
                os.system('cls')
                print("El jugador está registrado en la categoría:", category)
                
                while True:
                    try:
                        points_for = int(input("Ingrese la cantidad de puntos a favor del jugador: "))        
                        points_against = int(input("Ingrese la cantidad de puntos en contra del jugador: "))

                        player["PG"] += 1        
                        player["PJ"] += 1        
                        player["PA"] += points_for
                        player["PP"] += points_against
                        player["TP"] += player["PG"] * 2

                        # Calcular puntos a favor restando los puntos en contra
                        points_diff = points_for - points_against
                        player["PF"] += points_diff

                        # Determinar al ganador
                        if points_diff > 0:
                            print("¡El jugador es el ganador!")
                        elif points_diff < 0:
                            print("El jugador perdió.")
                        else:
                            print("El partido terminó en empate.")
                            
                        break
                    except ValueError:
                        print("Por favor, ingrese datos válidos.")
                
                print("Puntos actualizados:")
                print(player)
                os.system('pause')
                return category
        print("No se encontró el jugador en ninguna categoría.")
    os.system('cls')
    os.system('pause')
    
#Function por see the statistics of the player
def view_statistics(players_by_categories: dict) -> dict:
    name_player = str(input("Ingrese nombre del jugador: "))
    os.system('pause')

    for category, info in players_by_categories.items():
        for player in info["jugadores"]:
            if name_player == player["nombre"]:
                os.system('cls')
                print("El jugador está registrado en la categoría:", category)
                print("ID\t\tNombre\t\tPJ\tPG\tPP\tPA\tTP")
                print(f"{player['ID']}\t\t{player['nombre']}\t\t{player['PJ']}\t{player['PG']}\t{player['PP']}\t{player['PA']}\t{player['TP']}")
                os.system('pause')
                return

    print("Jugador no encontrado en ninguna categoría.")
    os.system('pause')
    return "Jugador no encontrado en ninguna categoría."

#Function por see the winners of each category
def get_winners(players_by_categories: dict) -> dict:
    ganadores = {}
    for categoria, infoCat in players_by_categories.items():
        if infoCat["jugadores"]:
            ganador = max(infoCat["jugadores"], key=points_in_favor)
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
