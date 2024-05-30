class Persona:
    def __init__(self, nombre, edad): #el constructor se define mediante un método llamado __init__.
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

# Crear un objeto de la clase Persona usando el constructor
persona2 = Persona('Ana', 25)
persona2.saludar()
