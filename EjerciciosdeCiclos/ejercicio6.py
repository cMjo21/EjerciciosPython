class Años:
    def __init__(self, edad):
        self.edad = edad

    def ingresedad(self):
        # Método para ingresar la edad
        self.edad = int(input("Ingresar edad: "))

    def calcularañoscumplidos(self):
        # Método para imprimir los años cumplidos
        print("Años cumplidos:")
        for i in range(1, self.edad + 1):
            print(i)


calcular = Años(edad=1)  

calcular.ingresedad()

calcular.calcularañoscumplidos()

