from __future__ import annotations
from abc import ABC
from datetime import date, datetime
from typing import List, Tuple

class Person(ABC):
    def __init__(self, name:str, dob:date):
        self._name = name
        self._dob = dob
    def __str__(self):
        return f"Name={self._name}, dob ={self._dob}, age={self.age}"
    @property
    def name(self)->str:
        return self._name
    @property
    def dob(self)->str:
        return self.dob
    @property
    def age(self)->int:
        return date.today().year - self._dob.year

# class Manager: # forward declaration
#     pass

class Employee(Person):
    _mgr: Manager
    def __init__(self, name, dob, ssn):
        super().__init__(name, dob)
        self._ssn = ssn
        self._mgr = None
    def __str__(self):
        return super().__str__() + f"ssn={self._ssn}"
    @property   
    def ssn(self)->str:
        return self._ssn
    @property
    def manager(self) -> Manager:
        return self._mgr
    @manager.setter
    def manager(self, m:Manager):
        if self._mgr:
            self._mgr.remove_employee(self)
        self._mgr = m

class Manager(Employee):
    _emps : List[Employee]
    def __init__(self, name, dob, ssn):
        super().__init__(name, dob, ssn)
        self._emps = []
    def add_employee(self,emp:Employee, *emps:Tuple[Employee]):
        for e in (emp, ) + emps:
            e.manager = self
            self._emps.append(e)
    def remove_employee(self, e:Employee):
        self._emps.remove(e)
    def __str__(self):
        ret =  super().__str__()
        tabs = '\t'
        m = self.manager
        while m:
            tabs += '\t'
            m = m.manager
        for e in self._emps:
            ret += f"\n{tabs}{e}"
        return ret

date_format = "%Y-%m-%d"
ceo = Manager("CEO", datetime.strptime("1970-1-1", date_format), "123-45-6789")
cfo = Manager("CFO", datetime.strptime("1970-1-1", date_format), "123-45-6789")
cto = Manager("CTO", datetime.strptime("1970-1-1", date_format), "123-45-6789")
ceo.add_employee(cfo, cto)
acc = Employee("Accountant", datetime.strptime("1970-1-1", date_format), "123-45-6789")
aud = Employee("Auditor", datetime.strptime("1970-1-1", date_format), "123-45-6789")
cfo.add_employee(acc, aud)
test = Employee("Tester", datetime.strptime("1970-1-1", date_format), "123-45-6789")
code = Employee("Coder", datetime.strptime("1970-1-1", date_format), "123-45-6789")
ba = Employee("Analyst", datetime.strptime("1970-1-1", date_format), "123-45-6789")
cto.add_employee(test,code,ba)
print(ceo)    