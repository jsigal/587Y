"""
Exercise 3.1 Collections and Slicing
Ex3_1_EndPoint.py
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

