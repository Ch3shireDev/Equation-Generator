from fractions import Element
from equations import Equation

e = Equation(1)
e.create_multiplication(-1, Element(1, 2))

x = Element(1,1)
y = Element(2,1)

print(x*y)
print(x/y)

print(e)
