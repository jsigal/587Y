class PersonInit:
    # def __init__(self, name):
    #     self._name = name
    #     self._age = 0
    def __init__(self, name, age = 0):
        self._name = name
        self._age = age
    def __str__(self):
        return f'my name is {self._name}, I am {self._age} years old'
    

ti = PersonInit('Thomas')
print(ti)
mc = PersonInit('Mimi', 10)
print(mc)



class PersonFactory:
    default_age_for_new_people = 1
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __str__(self):
        return f'my name is {self._name}, I am {self._age} years old'
    @classmethod
    def create_person_with_name(cls, name):
        print(cls)
        return PersonFactory(name, cls.default_age_for_new_people)
    @classmethod
    def create_person_with_name_and_age(cls,name, age):
        print(cls)
        return PersonFactory(name, age)   

ti = PersonFactory.create_person_with_name('Thomas')
print(ti)
mc = PersonFactory.create_person_with_name_and_age('Mimi', 10)
print(mc)