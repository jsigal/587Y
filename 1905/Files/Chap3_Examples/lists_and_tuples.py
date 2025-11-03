# List Indexing
airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'cdg']
print(airports[1])
airports[4] = airports[4].upper()
print(airports)

# List Slicing
airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
print(airports[1:2])
print(airports[3:])
print(airports[:])
print(airports[::-1])

# List Operators
north_airports = ['YYZ', 'ARN', 'LHS']
south_airports = ['SYD', 'RIO', 'CPT']
print(north_airports + south_airports)

# List Operations
airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
print(len(airports))
destinations = airports
if destinations is airports:
    print('Shared Reference')
    destinations[0] = 'SFO'
    print('airports changed', airports)
destinations = list(airports)
if destinations is not airports:
    print('Not Shared Reference')

# List Modifications
airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
airports[0] = 'LGA'
airports[2:3] = ['MSY', 'SFO']
print(airports)
airports.append('JFK')
airports.insert(0, 'SYD')
print(airports)
airports.sort()
print(airports)

# Tuple Operations

airports = ('LAX', 'HNL', 'YYZ', 'NRT', 'CDG')
print(airports[1:3])
print(airports[::-1])
north_airports = ['YYZ', 'ARN', 'LHS']
south_airports = ['SYD', 'RIO', 'CPT']
destinations = tuple(north_airports + south_airports)
print(destinations)

# Collections of Collections
north_airports = ('YYZ', 'ARN', 'LHS')
south_airports = ('SYD', 'RIO', 'CPT')
destinations = [north_airports, south_airports]
print(destinations)
print(destinations[0])
print(destinations[0][1])
print(destinations[0][1][2])
destinations.append(('LGA', 'JFK'))
print(destinations)

# Sequence Unpacking
airports = ('LAX', 'HNL', 'YYZ', 'NRT')
depart, layover1, layover2, arrive = airports
print(layover2)
depart, *layovers, arrive = airports
print(layovers)
depart, *rest = airports
print(rest)
