from geom2d import *

# Lists sorting
l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]


# def x(p):
#     return p.x


# def y(p):
#     return p.y

# First method
# l2 = sorted(l1, key=p.x)
# l2 = sorted(l1, key=p.y)

# Second method (lambda functions)
# l2 = sorted(l1, key=lambda p: p.x)
l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
print(l1)
print(l2)
