from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.__hp_actual = hp_actual
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_actual
        self.__energia_maxima = energia_maxima

    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter
    def hp_actual(self, nuevo_hp): #Metrodo de seguridad: La vida del pokemon cuando lo atanquen no puede mostrar que tiene vida negativa(-55)
        if nuevo_hp < 0: #Validamos la vida del pokemon, si la vida es negativa.
            nuevo_hp = 0 #Si es negativa nos va a mostrar 0, porque ya no tiene salud.
            self.__hp_actual = nuevo_hp #Guardamos ese valor en nuevo_hp y se le asigna a el atributo privado __hp_actual

    @property
    def energia_actual(self): 
        return self.__energia_actual
    
    @energia_actual.setter
    def energia_actual(self, nueva_energia): #Metodo de seguridad: La energia cuando se consuma no puede ser un numero negativo(-1)
        if nueva_energia < 0:
            nueva_energia = 0
            self.__energia_actual = nueva_energia
    
    @abstractmethod
    def atacar(self):
        pass
            
    def defender(self):
        # if opcion == 3:
        #     print(">>>Has usado: [DEFENDER]<<<")
        pass

    def descansar(self):
        #     print(">>>Has usado: [DESCANSO]<<<")
        pass

class PokemonAgua (Pokemon):pass

class PokemonFuego (Pokemon):pass

class PokemonPlanta (Pokemon):pass

class PokemonElectrico (Pokemon):pass