from abc import ABC, abstractmethod
import random

#Clase base "EL DISEÑO, PLANO, PLANTILLA"
class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.__hp_actual = hp_actual
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_actual
        self.__energia_maxima = energia_maxima
        self.defendiendo = False
        self.paralizado = False

#DECORADORES
    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter
    def hp_actual(self, nuevo_hp): #Metrodo de seguridad: La vida del pokemon cuando lo atanquen no puede mostrar que tiene vida negativa(-55)
        self.__hp_actual = nuevo_hp
        if nuevo_hp < 0: #Validamos la vida del pokemon, si la vida es negativa.
            nuevo_hp = 0 #Si es negativa nos va a mostrar 0, porque ya no tiene salud.
            self.__hp_actual = nuevo_hp #Guardamos ese valor en nuevo_hp y se le asigna a el atributo privado __hp_actual
        elif nuevo_hp > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo

    @property
    def energia_actual(self): 
        return self.__energia_actual
    
    @energia_actual.setter
    def energia_actual(self, nueva_energia): #Metodo de seguridad: La energia cuando se consuma no puede ser un numero negativo(-1)
        self.__energia_actual = nueva_energia
        if nueva_energia < 0:
            nueva_energia = 0
            self.__energia_actual = nueva_energia
        elif nueva_energia > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
    
    @abstractmethod
    def atacar(self, oponente):
        pass
            
    def defender(self):
        self.defendiendo = True
        if self.defendiendo == True:
            self.energia_actual = self.energia_actual - 5
            print(f"Se ha usado [DEFENSA], el daño recibido se reduce al mitad, has consumido [5 puntos] de Energia")

    def descansar(self):
        self.energia_actual = self.energia_actual + 20
        print(f"Se ha usado [DESCANSAR], la energia de: [{self.nombre}] se han restaurado [20 puntos] de energia")

        #BARRA DE SALUD DE LOS POKEMONES-----
    #Esta parte Sí fue con ayuda de IA porque queria agregar una barra de vida a los pokemones como el los juegos originales.
    def mostrar_estatus(self):
        # 1. Lógica de la barra (20 segmentos)
        unidades_vida = int((self.hp_actual / self.__hp_maximo) * 20)
        barra = "█" * unidades_vida + "░" * (20 - unidades_vida)
        
        # 2. Diseño visual estilo consola
        print(f"\n┌──────────────────────────────────────────┐")
        print(f"  {self.nombre.upper():<15} HP: {self.hp_actual}/{self.__hp_maximo}")
        print(f"  Lvl: 50         [{barra}]")
        print(f"  Energía: {self.energia_actual}/{self.__energia_maxima}")
        
        # 3. Mostrar estados si existen
        if self.paralizado:
            print(f"  ESTADO: [ PARALIZADO ⚡ ]")
        if self.defendiendo:
            print(f"  ESCUDO: [ ACTIVO 🛡️ ]")
        print(f"└──────────────────────────────────────────┘")
        print("="*30)

#CLASES HIJAS: Pokemones y sus tipos, movimientos.
class PokemonAgua (Pokemon):
    def atacar(self, oponente):
        if self.energia_actual >= 15: #Primero validamos si tenemos la energia suficiente para poder atacar
            self.energia_actual = self.energia_actual - 15 #Restamos los 15 puntos de nuestra energia, porque nosotros vamos a atacar
            daño = 20 #Usamos una variable para asignar el valor del daño base que tendrá nuestro pokemon, que son 20 puntos de daño 

            if isinstance(oponente, PokemonFuego):#Como son objetos lo que vamos a usar, validamos si lo que estamos usando es un objeto
                daño = 40
                print(f"[Ataque muy eficaz], el daño se multiplica el doble: [{daño} puntos]")
            else:
                print(f"[Ataque normal], no hay ventaja de tipos: [{daño} puntos]")

            if oponente.defendiendo == True:#validamos si el oponente esta usando defensa para poder reducir el daño a la mitad
                daño = daño // 2 #Con su defensa activa, el daño que recibe se divide entre 2 (y usamos // por si por alguna razon salen decimales)
                oponente.defendiendo = False#Entonces si al oponente se le reduce el daño es porque tiene la defensa activa, entonce ya hecha la reduccion, 
#                                                desactivamos su escudo porque terminó su turno
                print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")

            oponente.hp_actual = oponente.hp_actual - daño#El daño que va a recibir se lo restamos de sus puntos de salud
            print(f"¡{self.nombre} ha golpeado a {oponente.nombre}!")
            oponente.mostrar_estatus()
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")#Sino tenemos la energia suficiente no podemos atacar
            


class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual > 15:
            self.energia_actual = self.energia_actual - 15
            daño = 35

            if isinstance(oponente, PokemonPlanta):
                daño = 70
                print(f"[Ataque muy eficaz], el daño se multiplica el doble: [{daño} puntos]")
            else:
                print(f"[Ataque normal], no hay ventaja de tipos: [{daño} puntos]")

            if oponente.defendiendo == True:
                    daño = daño // 2
                    oponente.defendiendo = False
                    print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")

            oponente.hp_actual = oponente.hp_actual - daño
            print(f"¡{self.nombre} ha golpeado a {oponente.nombre}!")
            oponente.mostrar_estatus()
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")
            

        
class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual > 15:
            self.energia_actual = self.energia_actual - 15
            daño = 25

            if isinstance(oponente, PokemonAgua):
                daño = 50
                print(f"[Ataque muy eficaz], el daño se multiplica el doble: [{daño} puntos]")
            else:
                print(f"[Ataque normal], no hay ventaja de tipos: [{daño} puntos]")

            if oponente.defendiendo == True:
                    daño = daño // 2
                    oponente.defendiendo = False
                    print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")

            oponente.hp_actual = oponente.hp_actual - daño
            print(f"¡{self.nombre} ha golpeado a {oponente.nombre}!")
            oponente.mostrar_estatus()
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")
        


class PokemonElectrico(Pokemon): #Este tipo de pokemon es el unico que es diferente a los demas
    def atacar(self, oponente): #Usamos el metodo del padre atacar
        if self.energia_actual >= 15: #Validamos si tenemos energia suficiente
            self.energia_actual = self.energia_actual - 15 #Restamos la energia usada
            daño = 30#Asignamos nuestro daño base

            if random.random() <=0.2: #Justo aca usaremos LA LIBRERIA RANDOM y uno de sus METODOS RANDOM para que eliga si aplica la paralisis o no tiene un probabilidad del 20%
                oponente.paralizado = True #En caso de que random eliga un numero entre 0 y 0.2 cambiara el estado del oponente a paralizado
                print(f"[Efecto] El oponente esta PARALIZADO!")

            if isinstance(oponente, PokemonAgua): #Validamos si el objeto oponente pertenece a la clase PokemonAgua
                daño = 60 #Aginamos nuestro daño base
                print(f"[Ataque SUPER EFICAZ], el daño se multiplica el doble:[{daño}] ")

            if oponente.defendiendo == True: #Validaremos si el oponente tiene su defensa activa
                daño = daño // 2 #En caso de que sí vamos a reducir el daño del ataque a la mitad
                oponente.defendiendo = False #Desactivamos la defensa del oponente porque sino la tendría siempre activa y todos los ataque serian reducidos a la mitad
                print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")

            oponente.hp_actual = oponente.hp_actual - daño#Aqui restamos el daño hecho a la salud que tiene el oponente
            print(f"¡{self.nombre} ha golpeado a {oponente.nombre}!")
            oponente.mostrar_estatus()
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")
        
        

        