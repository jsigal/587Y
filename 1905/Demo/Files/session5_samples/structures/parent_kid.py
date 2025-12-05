from __future__ import annotations
from abc import ABC
from typing import List

class Person(ABC):
    """
    Docstring for Person
    """
    def __init__(self, name:str, dob:str):
        self._name = name
        self._dob = dob
    def __str__(self):
        return f"Name={self._name}, dob ={self._dob}"
    @property
    def name(self)->str:
        return self._name
    @property
    def dob(self)->str:
        return self.dob
    

# class Kid: # forward declaration
#     pass

class Parent(Person):
    _kids: List[Kid]
    def __init__(self, name, dob):
        super().__init__(name, dob)
        self._kids = []
    def add_kid(self, child: Kid):
        self._kids.append(child)
    def __str__(self):
        ret =  super().__str__()
        for k in self._kids:
            ret += "\n\t" + str(k)
        return ret

# class Toy: # forward declaration
#     pass

class Kid(Person):
    _toys: List[Toy]
    def __init__(self, name:str, dob:str, p:Parent):
        super().__init__(name, dob)
        self._parent = p
        self._toys = []
    def add_toy(self, t:Toy):
        self._toys.append(t)
    def __str__(self):
        ret =  super().__str__()
        for t in self._toys:
            ret += "\n\t\t" + str(t)
        return ret
    
class Toy:
    def __init__(self, name:str, rating:int):
        self._name = name
        self._rating = rating
    def __str__(self):
        return f'Name={self._name}, Rating={self._rating}'
    

if __name__ == '__main__':
    j = Parent("Josh", "9/10")
    t = Kid("Thomas", "11/11",j)
    m = Kid("Mimi", "11/30",j)
    t1 = Toy("Xbox", 10)
    t2 = Toy("Lego", 5)
    t3 = Toy("Barbie", 8)
    t4 = Toy("Imagination", 10)
    j.add_kid(t)
    j.add_kid(m)
    t.add_toy(t1)
    t.add_toy(t2)
    m.add_toy(t3)
    m.add_toy(t4)

    print(j)

