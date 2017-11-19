from geom2d import *

l1 = list(map(lambda i: Point(i, i*i), range(-5, 6)))

# l2 = list(map(lambda p: Point(p.x, -p.y), l1))

# l2 = list(filter(lambda p: p.x > 0, l1))
l2 = list(filter(lambda p: p.x % 2 == 0, l1))

print(l1)
print(l2)
