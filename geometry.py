from geom2d import *

l1 = []

for i in range(-5, 6):
    l1.append(Point(i, i*i))

l2 = []

for el in l1:
    l2.append(Point(el.x, -el.y))

print(l1)
print(l2)

# List comprehension
l1c = [Point(i, i*i) for i in range(-5, 6)]
l2c = [Point(el.x, -el.y) for el in l1c]

print("List comprehension")
print(l1c)
print(l2c)
