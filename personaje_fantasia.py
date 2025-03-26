'''Se va a crear un sistema para gestionar personajes de un 
juego de rol de fantasía. Cada personaje tendrá atributos 
básicos (nombre, raza, clase, nivel, vida, maná) 
y podrá equiparse con objetos y aprender habilidades.

Funciones:
Crea funciones para:
Crear instancias de Objeto y Habilidad.
Permitir al usuario interactuar con el personaje 
(equipar objetos, aprender habilidades, mostrar estado).
'''

class Personaje:
    inventario = []
    habilidades = []
    def __init__(self, nombre: str, raza: str, clase: str,
nivel= 1, vida= 10, mana= 5):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.nivel =nivel
        self.vida = vida
        self.mana = mana

    def equipar_objeto(self, objeto):
            self.inventario.append(objeto)
    
    def aprender_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Clase: {self.clase}, \
Nivel: {self.nivel}, Vida: {self.vida}, Mana: {self.mana}")
        
class Objeto:
    def __init__(self, nombre: str, descripcion: str, efecto: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.efecto = efecto
    def mostrar_objeto_cogido(self):
        print(f"Objeto encontrado: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Su efecto es: {self.efecto}")
        
class Habilidad:
    def __init__(self, nombre: str, descripcion: str, efecto: str, coste_mana: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.efecto = efecto
        self.coste_mana = coste_mana

def crea_personaje():
    heroe_nombre = input("Nombre de tu heroe: ")
    heroe_raza = input("De que raza es: ")
    heroe_clase = input("Indica su clase: ")
    global heroe;
    heroe = Personaje(heroe_nombre, heroe_raza, heroe_clase)

def conger_objeto():
    objeto_nombre = input("Que objeto es: ")
    objeto_descripcion = input("Describelo: ")
    objeto_efecto = input("Cual es su efecto: ")
    global objet;
    objet = Objeto(objeto_nombre, objeto_descripcion, objeto_efecto)

crea_personaje()
heroe.mostrar_estado()
conger_objeto()
objet.mostrar_objeto_cogido()