class Tabla:
    
    def __init__(self, numero_max, multiplicando):
        self.numero_max = numero_max
        self.multiplicando = multiplicando

    def tabla(self):
        for i in range(1, self.numero_max + 1):
            resultado = i * self.multiplicando
            print(f"{self.multiplicando} x {i} = {resultado}")
            
# Crear una instancia de la clase TablaMultiplicar
tabla_multiplicar = Tabla(numero_max=10, multiplicando=1)

# Llamar al método para imprimir la tabla de multiplicar
tabla_multiplicar.tabla()
        
        
        

