class Comida:
    def __init__(self, nombre, caracteristicas, precio):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        self.precio = precio

# Crear instancias de la clase Comida para diferentes platos
arroz_chino = Comida("Arroz Chino", "Delicioso arroz salteado con verduras y pollo", 15000)
sushi = Comida("Sushi", "Variados rollos de sushi fresco", 30000)
pizza = Comida("Pizza", "Masa crujiente con ingredientes variados", 20000)

# Lista de comidas
lista_comidas = [arroz_chino, sushi, pizza]

# Solicitar al usuario que ingrese el nombre de la comida
nombre_comida = input("Ingresa el nombre de la comida: ")

# Buscar la comida en la lista
comida_encontrada = None
for comida in lista_comidas:
    if comida.nombre.lower() == nombre_comida.lower():
        comida_encontrada = comida
        break

# Mostrar información sobre la comida si se encuentra
if comida_encontrada:
    print(f"\n{comida_encontrada.nombre}:")
    print(f"Características: {comida_encontrada.caracteristicas}")
    print(f"Precio: ${comida_encontrada.precio:.2f}")
else:
    print(f"No se encontró información para '{nombre_comida}'.")


# ingresa el nombre de la comida como 
# Sushi
# Arroz chino
# Pizza 


