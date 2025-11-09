def hello():
    print('hello')
def goodbye():
    print('bye')
hello()
goodbye()
hello()
goodbye()

print(hello, goodbye)

def print_kid(name='Snowball', age=2):
    print(f'the kid is named {name} and they are {age} years old')

# call the function with parameters by position
print_kid('Thomas',13)
# call the function with parameters by keyword
print_kid(age=10, name='Mimi')
# call the function with no parameters
print_kid()

def param_req(pos1, pos2, kw1, kw2, pos3=3, pos4=4, kw3=3, kw4=4):
    print(pos1, pos2, kw1, kw2, pos3, pos4, kw3, kw4)

param_req(1,2,3,4)
param_req(kw1=1,kw2=2,pos1=3,pos3=4, pos2=8)

def func_that_returns_data():
    return 'data'
ret = func_that_returns_data()
print(ret)

def func_that_returs_lots():
    return 1,2,3,4,5,6
ret = func_that_returs_lots()
print(type(ret),ret)

first, *middle, last = func_that_returs_lots()
print(first, middle, last)

mystr = "hello"
print(f'outside-before {mystr}')
def change_mystr(mystr):
    print(f'inside-before {mystr}')
    mystr="something else"
    print(f'inside-after {mystr}')
change_mystr(mystr)
print(f'outside-after {mystr}')

def func_with_lots_of_args_pos(*objects):
    print(f'the args are {objects}')
func_with_lots_of_args_pos()
func_with_lots_of_args_pos(1,'a')
func_with_lots_of_args_pos(1,2,3,4,5)

def func_with_lots_of_args_kw(**objects):
    print(f'the args are {objects}')
func_with_lots_of_args_kw()
func_with_lots_of_args_kw(a=1,b='a')
func_with_lots_of_args_kw(w=1,x=2,y=3,z=4,v=5)

def really_generic_func(*posargs, **kwargs):
    print(f'the pos args are {posargs}')
    print(f'the keyword args are {kwargs}')

really_generic_func()
really_generic_func(1,2,3)
really_generic_func(a=1,b=2,c=3)
really_generic_func(5,6,x=7,z=9)

def thefunc(a, b, c=1,d=2, *pos, **kw):
    pass



# calling a function passing in pos or kw args

# call the function with parameters by position
print_kid('Thomas',13)
# call the function with parameters by keyword
print_kid(age=10, name='Mimi')

ti = ('Thomas', 13)
print_kid(*ti)
mc = {"name":"Mimi", "age":10}
print_kid(**mc)

# monkey patch
print('calling hello()')
hello()
print('calling goodby()')
goodbye()

temp = hello
hello = goodbye
goodbye = temp

print('calling hello()')
hello()
print('calling goodby()')
goodbye()

tenp = goodbye
temp()
temp = hello
temp()

# labmda
def plus(x, y):
    return x + y

a = 1
b = 2

add = plus
add = lambda x,y : x + y

res = add(a,b)
print(res)
print(add, plus)
