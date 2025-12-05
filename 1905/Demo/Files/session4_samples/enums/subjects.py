from enum import Enum, unique

@unique
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   SCIENCE = 5
   SANSKRIT = 4

obj = subjects.MATHS
print (type(obj))



subjects = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
print(subjects.ENGLISH)
print(subjects.MATHS)
print(subjects.SCIENCE)
print(subjects.SANSKRIT)

obj = subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)