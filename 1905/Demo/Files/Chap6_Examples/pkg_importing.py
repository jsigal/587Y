# Package Example
import geometry.two_d.circles as ci
from geometry.three_d.volumes import cylinder_volume as cv

rad = 1.0
length = 2.0
ar = ci.area(rad)
print('circle area {}'.format(ar))
vol = cv(rad, length)
print('cylinder volume {}'.format(vol))
