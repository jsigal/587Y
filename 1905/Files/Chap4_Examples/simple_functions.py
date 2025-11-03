# Simple Function Example
def print_one():
    num = 1
    print('the value of num is', num)

def print_two():
    num = 2
    print('the value of num is', num)

print_one()
print_two()
print('The print_one object', print_one)

# Passing Data Into a Function
def printposit(depart, arrive):
    print('depart and arrive by position:', depart, arrive)

printposit('NRT', 'HNL')

# Keyword Parameters
def printkey(depart, arrive):
    print('depart and arrive by keyword:', depart, arrive)

def printdef(depart='LAX', arrive='HNL'):
    print('depart and arrive defaults:', depart, arrive)

printkey(arrive='HNL', depart='NRT')
printdef(depart='AMS')

# Variable-Length Parameter List Example
def printargs(*args, **kwargs):
    print('Positional', args)
    print('Keyword', kwargs)

printargs('Jean', 35, 97.85)
printargs(name='Jean', age=35, rate=97.85)
printargs('Employee', name='Jean', age=35, rate=97.85)

# The following would cause a syntax error
# SyntaxError: positional argument follows keyword argument
# printargs(name='Jean', age=35, rate=97.85, 'Employee')

# Variable-Length Argument Lists
employee1 = ['Jean', 35, 97.85]
employee2 = {'name': 'Jules', 'age': 29, 'rate': 89.99}
printargs(*employee1)
printargs(**employee2)
printargs(employee2)

# Parameters and Scope
def increment(number):
    number += 1
    print('function number is', number)

number = 5
increment(number)
print('global number is', number)

# Enclosed Functions
def logdata():
    def print_header():
        print('Beginning status')

    def print_footer():
        print('Ending status')

    print_header()
    print('Processing...')
    print_footer()

logdata()


# Scope
var = 'global'
def fun1():
    var = 'enclosing'

    def fun2():
        var = 'local'
        print('enclosed var:', var)

    fun2()
    print('enclosing var:', var)

fun1()
print('global var:', var)

# global statement
var = 'global'
def fun1():
    var = 'enclosing'

    def fun2():
        global var
        var = 'local'
        print(var)

    fun2()
    print(var)

fun1()
print(var)

# nonlocal statement
var = 'global'
def fun1():
    var = 'enclosing'

    def fun2():
        nonlocal var
        var = 'local'
        print(var)

    fun2()
    print(var)

fun1()
print(var)

# Function return Example
def addtwice(num):
    return num + num

def double_vals(arg):
    return arg, arg * 2

ans = addtwice(3)
print('ans is', ans)
first, second = double_vals('a')
print('first is', first, 'second is', second)

# Mutable and Immutable Arguments
def addone(num, handle):
    num += 1
    handle.append('ONE')
    print('Inside', handle, num)

name = ['Sam']
count = 0
addone(count, name)
print('Outside', name, count)

# Functions and Polymorphism
def twice(parm):
    return parm + parm

print('Try twice()', twice(5.5))
print('Try twice()', twice(['a', 'list']))
# The following will cause a Type exception to be raised
# print(twice({'firstname': 'Robert', 'lastname': 'Johnson'}))
