# Simple Testing
sea = 'atlantic ocean'
if sea.islower():
    print(sea.upper())
else:
    print(sea)

sea = input('Enter the sea name: ')
if sea != '' :
    print('sea is not empty')
else:
    print('sea is empty')

# Testing Alternatives Using elif
sea = input('Enter the sea name: ')
if sea.lower() == 'atlantic':
    print(sea, 'is deep')
elif sea.lower() == 'pacific':
    print(sea, 'is big')
elif sea.lower() == 'baltic':
    print(sea, 'is cold')
else:
    print(sea, 'is not big or cold')

# Assignment Expressions
sea = input('Enter the sea name: ')
if (name := sea.lower()) == 'atlantic':
    print(sea, 'is deep')
elif name == 'pacific':
    print(sea, 'is big')
elif name == 'baltic':
    print(sea, 'is cold')
else:
    print(sea, 'is not big or cold')

# The pass Statement
sea = input('Enter the sea name: ')
if (name := sea.lower()) == 'atlantic':
    print(sea, 'is cold')
elif name == 'pacific':
    pass
elif name == 'baltic':
    print(sea, 'is cold')
else:
    print(sea, 'is not big or cold')

# Explicit Line Continuation
if sea == 'Atlantic' or \
    sea == 'Pacific' or \
    sea == 'Indian':
    print(sea, 'is a well known sea')
else:
    print('Unknown sea')

# Implicit Line Continuation
if (sea == 'Atlantic' or
        sea == 'Pacific' or
        sea == 'Indian'):
    print(sea,
          'is a well known sea')
else:
    print('Unknown sea')
