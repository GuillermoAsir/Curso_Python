#Classes
class Animal:
    def __init__(self, species,sound, color="rojo", age: int = 0):
        self.species = species #Propiedad pública
        self.__sound = sound #Propiedad privada
        self._color = color #Propiedad protegida
        self.age = age

    def make_sound(self):
        #Metodo publico, que puede usarse por cualquier persona.
        print(f"El {self.species} hace {self.__sound}")
    
    def get_sound(self):
        #Metodo que usa el objeto epara acceder a la propieedad sound
        return self.__sound
    
    def grow_older(self):
        #Incrementa la edad en un año de la clase animal o objeto animal
        self.age += 1
        if self.age > 15:
            print(f"El {self.species} la palmado")
        else:
            print(f"El {self.species} ahora tiene {self.age}")


my_animal = Animal("Perro","Guau","azul", 15)
my_animal2 = Animal("Gato","Miau")

# print(type(my_animal))
# print(type(my_animal2))

# print(my_animal)

# print(my_animal.age)
# print(my_animal2.age)


# print (f"la especie es {my_animal._color} y tiene edad {my_animal.age} y la va a palmar")

# print(my_animal._color)

# my_animal.make_sound()

# print (my_animal.get_sound())

print (my_animal.grow_older())