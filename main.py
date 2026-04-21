from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
import random

def seleccionar_pokemon(nombre_entrenador):
        mostrar_catalogo_disponible()

        while True:
                opcion = input(f"{nombre_entrenador} elige el número de tu Pokémon: ")

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
                
def iniciar_juego():
        entrenador1 = input("Nombre del Jugador 1: ")
        jugador1 = seleccionar_pokemon(entrenador1)

        entrenador2 = "Computadora"
        jugador2 = seleccionar_pokemon(entrenador2)

        while jugador1.hp_actual > 0 and jugador2.hp_actual > 0:
                print(f"\nESTADO: {jugador1.nombre} ({jugador1.hp_actual} HP) vs {jugador2.nombre} ({jugador2.hp_actual} HP)")

                print("\n1. Atacar (15 energía)\n2. Defender\n3. Descansar")

                accion = input(f"{jugador1.nombre}, ¿qué harás?: ")

                if accion == "1":
                        if jugador1.energia_actual >= 15:
                                jugador1.atacar(jugador2) 
                        else:
                                print("Energía insuficiente")

                elif accion == "2":
                        jugador1.defendiendo = True
                        print(f"{jugador1.nombre} se defiende.")
                
                elif accion == "3":
                        jugador1.descansar()

                
                if jugador2.hp_actual <= 0:
                        print(f"¡{jugador2.nombre} ha sido derrotado!")
                        break
                


                
                print(f"\n--- Turno de la Computadora ({jugador2.nombre}) ---")
                if jugador2.energia_actual >= 15:
                        jugador2.atacar(jugador1)
                else:
                        jugador2.descansar()

                if jugador1.hp_actual <= 0:
                        print(f"¡{jugador1.nombre} ha sido derrotado! Fin del juego.")
                        break
iniciar_juego()