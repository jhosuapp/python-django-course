class Person:
    specie = 'humano'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def change_species(cls, specie):
        cls.specie = specie
        return specie
    
    @staticmethod
    def is_older(age):
        return age >= 18
        
    
person1 = Person("Jhosua", 24)
person2 = Person("Dana", 14)

print(person1.name, person1.age, person1.specie)
print(person2.name, person2.age, person2.specie)

Person.change_species("Cyber bot")

print(person1.name, person1.age, person1.specie, person1.is_older(person1.age))
print(person2.name, person2.age, person2.specie, person2.is_older(person2.age))
print(Person.is_older(18))