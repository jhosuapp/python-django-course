from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = 0
        
    def description(self):
        return f'El animal se llama {self.name} y tiene {self.age} años'
    
    def is_older(self):
        if(self.age > 10):
            return f'El animal es viejo'
        else:
            return f'El animal es joven'
    
    def _set_name(self, name):
        self.name = name
        return name
    
    def _get_name(self):
        return self.name
    
    def _set_age(self, age):
        self.age = age
        return age
    
    def _get_age(self):
        return self.age

    @abstractmethod
    def make_sound(self, sound):
        pass

class Dog(Animal):
    def make_sound(self, sound):
        return print('El animal', self.name, 'hace', sound)
    
    def bring_ball(self):
        return print(self.name, 'Esta trayendo la pelota')
    
class Cat(Animal):
    def make_sound(self, sound):
        return print('El animal', self.name, 'hace', sound)
    
class Bird(Animal):
    def make_sound(self, sound):
        return print('El animal', self.name, 'hace', sound)
    
    
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        print("Animales en el zoológico:")
        for animal in self.animals:
            print(animal.description())

    def make_sounds(self):
        print("\nTodos los animales haciendo sonidos:")
        for animal in self.animals:
            animal.make_sound("hace un sonido...")
            
            
dog = Dog("Jordan", 11)
cat = Cat("Billie", 7)
bird = Bird("Rebeca", 1)
zoo = Zoo()
            
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(bird)

zoo.list_animals()
zoo.make_sounds()