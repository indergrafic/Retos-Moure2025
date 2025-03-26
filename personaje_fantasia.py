'''Se va a crear un sistema para gestionar personajes de un 
juego de rol de fantasía. Cada personaje tendrá atributos 
básicos (nombre, raza, clase, nivel, vida, maná) 
y podrá equiparse con objetos y aprender habilidades.'''

class Personaje:
    inventario = []
    habilidades = []
    def __init__(self, nombre: str, raza: str, clase: str, 
                 nivel: int, vida: int, mana: int):
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
         print(f"Nombre: {self.nombre}, Raza: {self.raza}, Clase: {self.clase},\
              Nivel: {self.nivel}, Vida: {self.vida}, Mana: {self.mana}")
         