from fractions import Element
from equations import Equation
from random import randint

e = Equation(1)
for m, n, x, y in [[0, 4, 1, 5], [1, 3, 1, 5], [1, 2, 1, 4]]:
    e.complicate(m, n, x, y)

print(e)
