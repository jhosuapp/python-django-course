class Person:
    species = "human"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Protected
        self._energy = 100
        # Privated
        self.__password = "1234"
        
    def work(self):
        return f"{self.name} Está trabajando arduamente"
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    
    
person1 = Person("Jhosua", 24)
person1._waste_energy(10)

print(person1._energy)
# print(person1.__password)
print(person1._Person__password)