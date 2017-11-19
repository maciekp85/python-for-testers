from geom2d import *

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
# l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = list(l1)
l2[0] = Point(0, 0)

print(l1 == l2)
