from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.__hp_actual = hp_actual
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_actual
        self.__energia_maxima = energia_maxima
        self.defendiendo = False
        self.paralizado = False











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














class PokemonAgua (Pokemon):
    def atacar(self, oponente):
        if self.energia_actual >= 15: #Primero validamos si tenemos la energia suficiente para poder atacar
            self.energia_actual = self.energia_actual - 15 #Restamos los 15 puntos de nuestra energia, porque nosotros vamos a atacar
            daño = 20

            if isinstance(oponente, PokemonFuego):#Como son objetos lo que vamos a usar, validamos si lo que estamos usando es un objeto
                daño = 40
                print(f"[Ataque muy eficaz], el daño se multiplica el doble: [{daño} puntos]")
            else:
                daño = 20
                # oponente.hp_actual = oponente.hp_actual - daño_base
                print(f"[Ataque normal], no hay ventaja de tipos: [{daño} puntos]")

            if oponente.defendiendo == True:#validamos si el oponente esta usando defensa para poder reducir el daño a la mitad
                daño = daño // 2 #Con su defensa activa, el daño que recibe se divide entre 2 (y usamos // por si por alguna razon salen decimales)
                oponente.defendiendo = False#Entonces si al oponente se le reduce el daño es porque tiene la defensa activa, entonce ya hecha la reduccion, 
#                                                desactivamos su escudo porque terminó su turno
                print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")

            oponente.hp_actual = oponente.hp_actual - daño#El daño que va a recibir se lo restamos de sus puntos de salud
            print(f"Daño causado: [{daño}]")
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")#Sino tenemos la energia suficiente no podemos atacar
            


class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        pass
        

        
class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        pass
        

        

class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual >= 15:
            self.energia_actual = self.energia_actual - 15
            daño = 20

            if random.random() <=0.2:
                oponente.paralizado = True
                print(f"[Efecto] El oponente esta PARALIZADO!")

            if isinstance(oponente, PokemonAgua):
                daño = 40
                print(f"[Ataque SUPER EFICAZ], el daño se multiplica el doble:[{daño}] ")

            if oponente.defendiendo == True:
                daño = daño // 2
                oponente.defendiendo = False
                print(f"El oponente ha usado [DEFENDER], el daño se ha reducido a la mitad.")


            oponente.hp_actual = oponente.hp_actual - daño
        else:
            print(f"Energia insuficiente: [{self.energia_actual}]")
        
        

        