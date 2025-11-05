# from Statement
from circles import area
from volumes import cylinder_volume as cv

rad = 1.0
length = 2.0
ar = area(rad)
print('circle area {}'.format(ar))
vol = cv(rad, length)
print('cylinder volume {}'.format(vol))