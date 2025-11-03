class Person:
    def __init__(self, name):
        self.name = name

def check_person():
    testname = 'Katrina'
    student = Person(testname)
    if student.name == testname:
        print('Person constructor ok')

if __name__ == '__main__':
    check_person()