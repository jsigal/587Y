# Using Standard Library and Documentation

import datetime

# Below are two strings that represent a date and time
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'

# Import the needed modules to convert both strings into datetime objects

# Compare these datetime objects using > to decide which is later

depdt = datetime.datetime.fromisoformat(depdt)
arrdt = datetime.datetime.fromisoformat(arrdt)

order = 'Follows' if arrdt > depdt else 'Preceedes'
print(arrdt, order, depdt)
