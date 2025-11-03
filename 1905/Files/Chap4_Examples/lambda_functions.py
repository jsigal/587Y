# The sorted() Function
costs = (('YYZ', '35'), ('HNL', '100'), ('NRT', '52.5'))
print(sorted(costs))
print(sorted(costs, key=lambda p: p[1]))
print(sorted(costs, key=lambda p: float(p[1])))

# Functions as Arguments
def print_german():
    print('Guten Morgen')

def print_italian():
    print('Buon Giorno')

def print_greeting(lang, lang_func):
    print('Good Morning in', lang, 'is', end=' ')
    lang_func()

print_greeting('German', print_german)
print_greeting('Italian', print_italian)

# Hiding Function Calls in Lambda Expressions
def print_german(name):
    print('Guten Morgen', name)

def print_italian(name):
    print('Buon Giorno', name)

def print_greeting(lang, lang_func):
    print('Good Morning in', lang, 'is', end=' ')
    lang_func()

print_greeting('German', lambda: print_german('Hans'))
print_greeting('Italian', lambda: print_italian('Gina'))
