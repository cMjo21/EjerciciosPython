
class Educativo:
    def __init__(self):
        self.nota = float(input("Ingrese la nota final: "))

    def calcularnotav(self):
        print(f"Perdida la materia en {self.nota} sin tener recuperación") if self.nota < 1.0 else None
        if 1.0 <= self.nota <= 2.9:
            recuperacion = self.obtener_nota_recuperacion()
            self.imprimir_resultado_recuperacion(recuperacion)
        elif 3.0 <= self.nota <= 3.5:
            print(f"Aceptable {self.nota} por recuperación")
        elif 3.6 <= self.nota <= 3.9:
            print(f"Aceptable {self.nota} sin recuperación, te recomiendo que sigas mejorando, vas bien")
        elif 4.0 <= self.nota <= 4.5:
            print(f"Excelente {self.nota} vas por un buen camino hacia el éxito")
        elif 4.6 <= self.nota <= 5.0:
            print(f"Cientifico {self.nota} tienes un gran futuro adelante")

    def obtener_nota_recuperacion(self):
        return float(input("Ingrese la nota de recuperación: "))

    def imprimir_resultado_recuperacion(self, recuperacion):
        if 1.0 <= self.nota <= 2.5 and 3.0 <= recuperacion <= 5:
            print(f"Perdido la materia en {self.nota} pero se puede nivelar máximo nota final 3.0")
        elif 2.5 <= self.nota <= 2.9 and 3.0 <= recuperacion <= 5:
            print(f"Perdido la materia en {self.nota} pero se puede nivelar máximo nota final 3.5")

notasuno = Educativo()
notasuno.calcularnotav()
