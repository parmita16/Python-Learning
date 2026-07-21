import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

print("Distance = {:.2f}".format(distance))
print("Midpoint = ({:.2f}, {:.2f})".format(mid_x, mid_y))