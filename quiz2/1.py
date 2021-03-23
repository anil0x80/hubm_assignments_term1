import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = math.pow(b, 2) - 4*a*c
if discriminant < 0:
    sys.exit("There are no solutions")  # no need to go further at this point
elif discriminant > 0:
    print("There are two solutions")
else:
    print("There is one repeated solution")

x1 = (-b + math.sqrt(discriminant)) / (2*a)
x2 = (-b - math.sqrt(discriminant)) / (2*a)

# match output precision as shown at quiz instruction
if x1 != x2:
    print("Solution(s): {:.2f} {:.2f}".format(x1, x2))
else:
    print("Solution(s): {:.2f}".format(x1))

