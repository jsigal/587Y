"""
Exercise 3.1 Collections and Slicing
Ex3_1.py
"""

# Part A
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY', 'LAX']
flightlist = ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4]

first,second, *rest, secondlast, lastlast = codelist
print(f'first two {first}, {second}')
print(f'last two {secondlast}, {lastlast}')


# departcity = flightlist[0]
# arrivecity = flightlist[1]
# departdaytime = flightlist[2]
# arrivedaytime = flightlist[3]
# cost = flightlist[4]
# code = flightlist[5]

departcity, arrivecity, departdaytime, arrivedaytime, cost, code = flightlist
print(departcity, arrivecity, departdaytime, arrivedaytime, cost, code)

# step 4
print(codelist)
codelist.reverse()
print(codelist)


# step 5
print(codelist)
codelist.sort()
print(codelist)

# step 6
aptlist = codelist
print(codelist)
aptlist.pop()
print(codelist)
print(aptlist)