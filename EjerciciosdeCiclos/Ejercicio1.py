
class TablaMulti:
    # Atributo de clase
    numero = int(input("Ingrese un número: "))
    
    # Método constructor
    def __init__(self):
        self.resultado = None 
       
      
   # Método para imprimir y multiplicar 
    def mostrar(self):
         
        self.resultado = [self.numero * i for i in range(1, 11)]
                 
        print("El número es", self.numero)
        print("El resultado es ", self.resultado)
           

# Crear una instancia de la clase TablaMulti
multiplicacion = TablaMulti()

# Llamar al método para mostrar
multiplicacion.mostrar()
    



