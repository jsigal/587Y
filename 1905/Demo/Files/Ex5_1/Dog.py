class Dog:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    def haveBirthday(self):
        self._age +=1
        if self._age > 100:
            self.gettingOld = True
    def __str__(self):
        return f'My name is {self._name} and I am {self._age} years old'
    @property
    def age(self) -> int:
        return self._age
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value):
        yes = input('you really want to change the animal name?')
        if yes.lower().startswith('y'):
            self._name = value

dino = Dog("Dino", 70)
# print(dino.name, dino.age)
print(dino)
dino.haveBirthday()
# print(dino.name, dino.age)
print(dino)
print(dino.age)
print(dino.name)
dino.name = 'Fred'
print(dino.name)