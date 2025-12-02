
from abc import ABCMeta, abstractmethod


class OzAnimal(metaclass=ABCMeta):
    def __init__(self, fur_color):
        self._fur_color = fur_color
    def __str__(self):
        return f'Oz Animal with {self._fur_color} fur'
    @abstractmethod
    def speak(self):
        pass

class Lion(OzAnimal):
    def __str__(self):
        return super().__str__() + f' and I am a Lion'
    def speak(self):
        print('roar')
    # def speak_old(self):
    #     print('roar')
    # def speak_old2(self):
    #     print('roar')

class Tiger(OzAnimal):
    def __str__(self):
        return super().__str__() + f' and I am a Tiger'
    def speak(self):
        print('growl')

class Bear(OzAnimal):
    def __str__(self):
        return super().__str__() + f' and I am a Bears'
    def speak(self):
        print('grrrr')

oz = [Lion('sandy'),
    Tiger('orange stripes'), Bear('brown')]
for a in oz:
    print(a)  
    a.speak()  

# a = OzAnimal('blah')
# print(a)