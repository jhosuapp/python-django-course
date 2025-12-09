class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return f"{self.name} Está trabajando arduamente"
    
    
person1 = Person("Jhosua", 24)
person2 = Person("Dana", 14)

print(person1.name, person1.age)
print(person2.name, person2.age)