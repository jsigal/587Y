# The match Pattern Types
bow = input("Enter the body of water ")
match bow.lower():
    case 'atlantic':
        print(bow, 'Exact match')
    case 'pacific' | 'indian':
        print(bow, 'Loose match')
    case other:
        print(other, 'not a match')

# match Example
bow = input("Enter the body of water ")
match name:= bow.lower().split():
    case [ocean_name, 'ocean'] | [ocean_name, 'sea']:
        print(ocean_name, 'is large')
    case ['gulf', 'of', gulf_name]:
        print(gulf_name, 'is warm')
    case ['lake', lake_name]:
        print(lake_name, 'is fresh water')
    case [river_name, 'river']:
        print(river_name, 'flows downhill')
    case _:
        print(' '.join(name), 'is unknown')
