# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  Find intersection point between a ray and the Earth reference ellipsoid.
# Parameters:
#  d_l_x: x-component of origin-referenced ray direction
#  d_l_y: y-component of origin-referenced ray direction
#  d_l_z: z-component of origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin
#
# Output:
#  Intersection point between ray and reference ellipsoid.
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
l_d = [float('nan'), float('nan'), float('nan')]

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print('Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z')
    exit()

# write script below this line
R_E_M = R_E_KM * 1000
a = (d_l_x**2 + d_l_y**2 + d_l_z**2) / (1 - E_E**2)
b = 2 * ((d_l_x * c_l_x + d_l_y * c_l_y + d_l_z * c_l_z) / (1 - E_E**2))
c = (c_l_x**2 + c_l_y**2 + c_l_z**2) / (1 - E_E**2) - R_E_M
d_pls = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
d_mns = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

if d_pls > 0:
    d = d_pls
else:
    d = d_mns

l_d[0] = d * d_l_x + c_l_x
l_d[1] = d * d_l_y + c_l_y
l_d[2] = d * d_l_z + c_l_z

# output script
print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
