"""
Exercise 3.1 Collections and Slicing
Ex3_1_EndPoint_Bonus.py
"""

# Part A
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY', 'LAX']
flightlist = ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4]

print('The first two airport codes are', codelist[:2])
print('The last two airport codes are', codelist[-2:])

# departcity = flightlist[0]
# arrivecity = flightlist[1]
# departdaytime = flightlist[2]
# arrivedaytime = flightlist[3]
# cost = flightlist[4]
# code = flightlist[5]

departcity, arrivecity, departdaytime, arrivedaytime, *rest = flightlist

print('Using sequence unpacking')
print('The flight travels from', departcity, 'to', arrivecity)
print('The flight departs on', departdaytime, 'and arrives on', arrivedaytime)

codelist.reverse()
print('the reversed codelist', codelist)

codelist.sort()
print('the sorted codelist', codelist)

aptlist = codelist
aptlist.pop()
print('codelist', codelist)
print('aptlist', aptlist)

if codelist is aptlist:
    print('codelist and aptlist are shared')
else:
    print('codelist and aptlist are not shared')

aptlist = list(codelist)
aptlist.pop()
print('codelist after pop', codelist)
print('aptlist after pop', aptlist)

aptlist = codelist[:]
if codelist == aptlist:
    print('codelist and aptlist are equal')
else:
    print('codelist and aptlist are not equal')
if codelist is aptlist:
    print('codelist and aptlist are shared')
else:
    print('codelist and aptlist are not shared')

codelist.insert(0, 'ABC')
codelist.append('XYZ')
print(codelist)

codetupe = tuple(codelist)
if len(codetupe) == len(codelist):
    print('codetupe and codelist are equal length after tupling')
else:
    print('codetupe and codelist are not equal length after tupling')
if codetupe == codelist:
    print('codetupe and codelist are equal value after tupling')
else:
    print('codetupe and codelist are not equal value after tupling')
print(codelist)
print(codetupe)
print(type(codelist), type(codetupe))
if codetupe == tuple(codelist):
    print('codetupe and codelist are equal value after double tupling')
else:
    print('codetupe and codelist are not equal value after double tupling')
if codetupe[:] == codelist[:]:
    print('codetupe and codelist are equal value after slice tupling')
else:
    print('codetupe and codelist are not equal value after slice tupling')
print(type(codelist[:]), type(codetupe[:]))

codetupe = tuple(sorted(codetupe, reverse=True))
print('new codetupe', codetupe)
