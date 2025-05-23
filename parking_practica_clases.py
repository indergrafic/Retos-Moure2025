class Parking: 
    num_plaza = ['A1', 'A2', 'A3', 'A4', 'A5', 'A7', 'A8']
    def __init__(self, modelo, matricula):
        self.modelo = modelo
        self.matricula = matricula
        self.matri_plaza = {}

    def entrada(self):
        if len(self.num_plaza) > 0:
            plaza = self.num_plaza.pop(0)
            self.matri_plaza[self.matricula] = plaza
            print(f"Su plaza de aparcamiento es {plaza}")
            print("Ya puede pasar.")
            print(f"{self.matri_plaza}")
            print(f"{self.num_plaza}")

    def salida(self, matricula):
        print("Gracias por hacer uso de nuestro parking.")
        if matricula in self.matri_plaza:
            plaza = self.matri_plaza[matricula]
            del self.matri_plaza[matricula]
            self.num_plaza.append(plaza)
            print(f"La plaza {plaza} ha quedado libre")
        else:
            print("Matricula no encontrada en el parking.")

    def registro_plazas(self):
        listado = self.matri_plaza

        for placa, zona in listado.items():
            print(f"El conche con matricula {placa}, se encuentra aparcado en {zona}")

auto1 = Parking("Toyota", "1234GGH")
auto1.entrada()
auto2 = Parking("Ford", "3568UEC")
auto2.entrada()
auto2.registro_plazas()