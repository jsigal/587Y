# Chained Imports
import volumes

rad = 1.0
length = 2.0
ar = volumes.circles.area(rad)
print('circle area {}'.format(ar))
vol = volumes.cylinder_volume(rad, length)
print('cylinder volume {}'.format(vol))