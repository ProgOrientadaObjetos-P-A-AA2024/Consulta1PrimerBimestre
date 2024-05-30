class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asigna el parámetro nombre al atributo de instancia nombre
        self.edad = edad      # Asigna el parámetro edad al atributo de instancia edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

    def mostrar_edad(self):
        print(f"{self.nombre} tiene {self.edad} años.")

# Crear una instancia de la clase Perro
mi_perro = Perro('Firulais', 5)

# Llamar a los métodos de la instancia mi_perro
mi_perro.ladrar()          # Salida: Firulais está ladrando.
mi_perro.mostrar_edad()    # Salida: Firulais tiene 5 años.
