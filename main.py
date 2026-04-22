from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
import random

def menu_principal():
        while True:
                # print("="*45)
                # print(f"{'POKEMON ROJO FUEGO':^45s}")
                # print("="*45)
                # print(f"\n[1] 🕹️  Modo Jugador vs CPU:\n{'Entrenador vs Computadora':^25}\n\n[2] ⚔️  Modo Jugador vs Jugador:\n{'Duelo de Maestros':^25}\n\n[3] 🚪 Salir :\n{'Salir del Gimnasio':^25}\n")
                # modo = input(">>>Selecciona tu camino: ")

                print("\n" + "╔" + "═"*43 + "╗")
                print(f"║{'🏆 POKÉMON ROJO FUEGO 🏆':^41s}║")
                print("╠" + "═"*43 + "╣")
                print(f"║ [1] 🕹️  Jugador vs CPU{' ':^21s}║")
                print(f"║ [2] ⚔️  Jugador vs Jugador{' ':^17s}║")
                print(f"║ [3] 🚪 Salir{' ':^30s}║")
                print("╚" + "═"*43 + "╝")
                modo = input(">> Selecciona una opción: ")

                if modo == "1":
                        iniciar_juego(segundo_jugador_cpu=True)
                elif modo == "2":
                        iniciar_juego(segundo_jugador_cpu=False)
                else:
                        print("Has salido del juego!")
                        break

def seleccionar_pokemon(nombre_entrenador, opcion_fija=None ):
        mostrar_catalogo_disponible()

        while True:
                # print("="*45)
                # print(f"{'ELIJE TU POKEMON PARA LA BATALLA':^45S}")
                # print("="*45)
                if opcion_fija is None: # Si es un jugador
                        opcion = input(f"{nombre_entrenador} elige el número de tu Pokémon: ")
                else: # Si es la computadora
                        opcion = opcion_fija #Aqui se guarda el número que generamos al azar


                if opcion in CATALOGO_POKEMON:#Si esa opcion existe en el catalogo
                        info_pokemon = CATALOGO_POKEMON[opcion]
                        tipo = info_pokemon["tipo"]

                if tipo == "Fuego":
                        return PokemonFuego(info_pokemon["nombre"], info_pokemon["hp_maximo"], info_pokemon["hp_maximo"], info_pokemon["energia_maxima"], info_pokemon["energia_maxima"])
                
                if tipo == "Agua":
                        return PokemonAgua(info_pokemon["nombre"], info_pokemon["hp_maximo"], info_pokemon["hp_maximo"], info_pokemon["energia_maxima"], info_pokemon["energia_maxima"])
                
                if tipo == "Planta":
                        return PokemonPlanta(info_pokemon["nombre"], info_pokemon["hp_maximo"], info_pokemon["hp_maximo"], info_pokemon["energia_maxima"], info_pokemon["energia_maxima"])
                
                if tipo == "Electrico":
                        return PokemonElectrico(info_pokemon["nombre"], info_pokemon["hp_maximo"], info_pokemon["hp_maximo"], info_pokemon["energia_maxima"], info_pokemon["energia_maxima"])
                
def iniciar_juego(segundo_jugador_cpu = True):
        entrenador1 = input("Nombre del Jugador 1: ")
        jugador1 = seleccionar_pokemon(entrenador1)

        if segundo_jugador_cpu == True:
                entrenador2 = "Computadora"
                opcion_random = str(random.randint(1, 8)) # Elige un numero entre 1 y 8
                jugador2 = seleccionar_pokemon(entrenador2, opcion_fija=opcion_random)
        else:
                entrenador2 = input("Nombre del Jugador 2: ")
                jugador2 = seleccionar_pokemon(entrenador2)

        while jugador1.hp_actual > 0 and jugador2.hp_actual > 0:

                # orden = [1, 2]
                # random.shuffle(orden) #Esto hace que se eliga quien inicia la partida
                # print(f"Inicia el Jugador {orden[0]}!")

                # print("\n" + "="*45)
                # jugador1.mostrar_estatus() #Esto muestra las barras de estadisticas de los entrenadores
                # jugador2.mostrar_estatus()
                # print("="*45)

                print("\n" + "┌" + "─"*43 + "┐")
                print(f"│{'⚔️  TORNEO DE LOS OCHO MAESTROS ⚔️':^45s}│")
                print(f"│{'> Estadio Puntera <':^43s}│")
                print("├" + "─"*43 + "┤")

                jugador1.mostrar_estatus()#Esto muestra las barras de estadisticas de los entrenadores

                print(f"│{'ENTRENADOR vs RIVAL':^42s}│")

                jugador2.mostrar_estatus()#Esto muestra las barras de estadisticas de los entrenadores
                
                print("└" + "─"*43 + "┘")

                print(f"\n>> TURNO DE {entrenador1.upper()} ({jugador1.nombre}) <<")
                print("\n [1]. Atacar💥(15⚡) \n [2]. Defender🛡️ (5⚡) \n [3]. Descansar💤 (+20⚡)")
                accion = input(f"{jugador1.nombre} ELIGE: ")

                if accion == "1":
                        if jugador1.energia_actual >= 15:
                                jugador1.atacar(jugador2) 
                        else:
                                print("Energía insuficiente")
                                
                elif accion == "2":
                        jugador1.defendiendo = True
                        print(f"{jugador1.nombre} se defiende")
                
                elif accion == "3":
                        jugador1.descansar()
                
                if jugador2.hp_actual <= 0:
                        # print(f"\n¡{jugador2.nombre} se ha debilitado! {entrenador1} gana la batalla")
                        # break
                        jugador1.mostrar_estatus()
                        jugador2.mostrar_estatus()
    
                        print("\n" + "═"*45)
                        print(f" ¡{jugador2.nombre.upper()} SE HA DEBILITADO!")
                        print(f" 🏆 ¡EL GANADOR ES {entrenador1.upper()}! 🏆")
                        print("═"*45)
                        break
                
                #Aqui es donde la computadora decide que va a hacer de forma aleatoria con la libreria random
                #Asignamos a una variable la opcion aleatoria que elija el cpu, usamos el metodo choice para que escoja entre una lista de numeros que son nuestras opciones de juego
                
                # Turno del Jugador 2  o cpu
                if segundo_jugador_cpu:
                        print(f"\n--- TURNO DEL RIVAL(CPU) ({jugador2.nombre}) ---")
                        accion_2 = random.choice(["1", "2", "3"])
                else:
                        print(f"\n--- TURNO DE: {entrenador2.upper()} ({jugador2.nombre}) ---")
                        print("1. Atacar (15 energía)\n2. Defender\n3. Descansar")
                        accion_2 = input(f"{entrenador2} ELIGE: ")

                if accion_2 == "1":
                        if jugador2.energia_actual >= 15:
                                jugador2.atacar(jugador1)
                        else:
                                print(f"{jugador2.nombre} no tiene energía suficiente")
                elif accion_2 == "2":
                        jugador2.defendiendo = True
                        print(f"{jugador2.nombre} se defiende")

                elif accion_2 == "3":
                        jugador2.descansar()

                        # print("\n" + "═"*15 + " FIN DE LA BATALLA " + "═"*15)
                        # jugador1.mostrar_estatus()
                        # jugador2.mostrar_estatus()

                        # ganador = entrenador1 if jugador2.hp_actual <= 0 else (entrenador2 if not segundo_jugador_cpu else "CPU")
                        # print(f"\n🏆 ¡EL GANADOR ES {ganador.upper()}! 🏆")
                        # bre
                
                
                if jugador1.hp_actual <= 0 or jugador2.hp_actual <= 0:
                        
                        if jugador1.hp_actual <= 0:
                                ganador = "La Computadora" if segundo_jugador_cpu else entrenador2
                                perdedor = jugador1.nombre
                        else:
                                ganador = entrenador1
                                perdedor = jugador2.nombre
                        
                        print("\n" + "═"*45)
                        print(f"  ¡{perdedor.upper()} SE HA DEBILITADO!")
                        print(f"  🏆 ¡EL GANADOR ES {ganador.upper()}! 🏆")
                        print("═"*45)
                        break 

menu_principal()
