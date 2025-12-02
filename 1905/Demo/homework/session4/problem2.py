# Build a class Employee with multiple constructors 
# that can initialize an employee object in different ways.

class EmployeeSimple:
    def __init__(self, name: str, idnum : int =None, department:str=None):
        self._name = name
        self._idnum = idnum
        self._department = department
    def __str__(self):
        ret = f'Name: {self._name}'
        if self._idnum:
            ret += f' Id: {self._idnum}'
        if self._department:
            ret += f' Department: {self._department}'
        return ret
    @property
    def name(self):
        return self._name
    @property
    def idnum(self):
        return self._idnum
    @property
    def department(self):
        return self._department
    
e1 = EmployeeSimple('Thomas')
print(e1)
e2 = EmployeeSimple('Mimi', 101)
print(e2)
e3 = EmployeeSimple('Snowball', 201, "Cats")
print(e3)
e4 = EmployeeSimple('Garfield', 201, "Cats")
print(e4)

class EmployeeClassMethod:
    @classmethod
    def create_emp_with_name(cls, name):
        return EmployeeClassMethod(name)
    @classmethod
    def create_emp_with_name_id(cls, name, id):
        return EmployeeClassMethod(name, id)
    @classmethod
    def create_emp_with_name_dept(cls, name, dept):
        return EmployeeClassMethod(name, department=dept)
    @classmethod
    def create_emp_with_name_id_dept(cls, name, id, dept):
        return EmployeeClassMethod(name, id, dept)
    def __init__(self, name: str, idnum:int =None, department:str=None):
        self._name = name
        if idnum:
            self._idnum = idnum
        if department:
            self._department = department
    def __str__(self):
        ret = f'Name: {self._name}'
        if hasattr(self,'_idnum'):
            ret += f' Id: {self._idnum}'
        if hasattr(self,'_department'):
            ret += f' Department: {self._department}'
        return ret

e1 = EmployeeClassMethod.create_emp_with_name('Thomas')
print(e1)
e2 = EmployeeClassMethod.create_emp_with_name_id('Mimi', 101)
print(e2)
e3 = EmployeeClassMethod.create_emp_with_name_dept('Snowball', "Cats")
print(e3)
e4 = EmployeeClassMethod.create_emp_with_name_id_dept('Garfield', 201, "Cats")
print(e4)