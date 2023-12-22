class Nomina:
    def __init__(self, identificacion, nombre, cargo, salario):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def mostrar_empleado(self):
        print("Identificación:", self.identificacion)
        print("Nombre del empleado:", self.nombre)
        print("Cargo:", self.cargo)
        print("Salario:", self.salario)


class Aportes(Nomina):
    def __init__(self, identificacion, nombre, cargo, salario):
        super().__init__(identificacion, nombre, cargo, salario)

    def calcular_aportes(self):
        aporte_salud = round(self.salario * 0.085, 2)
        aporte_pension = round(self.salario * 0.12, 2)

        return {
            "Aporte Salud": aporte_salud,
            "Aporte Pensión": aporte_pension,
        }


class PrestacionesSociales(Nomina):
    def __init__(self, identificacion, nombre, cargo, salario):
        super().__init__(identificacion, nombre, cargo, salario)

    def calcular_prestaciones(self, dias_laborados):
        
        if self.salario <= 1160000:
            prima_servicios = round((self.salario + 140606) * dias_laborados / 360, 2)
            aporte_pension = round(self.salario * 0.12, 2) 
            return {
            "Prima de Servicios": prima_servicios,
            "Aporte Pensión": aporte_pension,
            "Dias laborados": dias_laborados,
            "Auxiliop de transporte": True 
            
            }
        
        elif self.salario > 1160000:
            
            prima_servicios = round(self.salario * dias_laborados / 360, 2)

        aporte_pension = round(self.salario * 0.12, 2)

        return {
            "Prima de Servicios": prima_servicios,
            "Aporte Pensión": aporte_pension,
            "Dias laborados": dias_laborados,
            "Auxiliop de transporte": False 
        }


# Crear instancia de PrestacionesSociales para el empleado1
empleado1 = PrestacionesSociales(identificacion=22333, nombre="Homero simpson", cargo="Analista", salario=1160000)
empleado1.mostrar_empleado()

# Calcular y mostrar los aportes del empleado1
aportes_empleado1 = Aportes(identificacion=empleado1.identificacion, nombre=empleado1.nombre,
                            cargo=empleado1.cargo, salario=empleado1.salario)
resultados_aportes = aportes_empleado1.calcular_aportes()

print("\nAportes del empleado1:")
for key, value in resultados_aportes.items():
    print(f"{key}: {value}")

# Calcular y mostrar las prestaciones sociales del empleado1
resultados_prestaciones = empleado1.calcular_prestaciones(dias_laborados=30)

print("\nPrestaciones Sociales del empleado1 dias laborados:")
for key, value in resultados_prestaciones.items():
    print(f"{key}: {value}")

# Calcular y mostrar el salario total del empleado1
salario_total_empleado1 = round(empleado1.salario + sum(resultados_aportes.values()) + sum(resultados_prestaciones.values()), 2)

print("\nSalario Total del empleado1:", salario_total_empleado1)



# Crear instancia de PrestacionesSociales para el empleado2 


empleado2 = PrestacionesSociales(identificacion=1111, nombre="bart simpson ", cargo="analista2", salario=2320000)
empleado2.mostrar_empleado()

# Calcular y mostrar los aportes del empleado2
aportes_empleado2 = Aportes(identificacion=empleado2.identificacion, nombre=empleado2.nombre,
                            cargo=empleado2.cargo, salario=empleado2.salario)
resultados_aportes = aportes_empleado2.calcular_aportes()

print("\nAportes del empleado2:")
for key, value in resultados_aportes.items():
    print(f"{key}: {value}")

# Calcular y mostrar las prestaciones sociales del empleado2
resultados_prestaciones = empleado2.calcular_prestaciones(dias_laborados=30)

print("\nPrestaciones Sociales del empleado2 dias laborados:")
for key, value in resultados_prestaciones.items():
    print(f"{key}: {value}")

# Calcular y mostrar el salario total del empleado2
salario_total_empleado2 = round(empleado2.salario + sum(resultados_aportes.values()) + sum(resultados_prestaciones.values()), 2)

print("\nSalario Total del empleado2:", salario_total_empleado2)



