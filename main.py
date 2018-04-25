from fractions import Element
from equations import Equation

e = Equation(1)
e.create_multiplication(-1, Element(2, 3))
print(e)