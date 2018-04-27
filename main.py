from fractions import Element
from equations import Equation
from random import randint

e = Equation()
print('[')
for i in range(10):
    m, n, x, y = randint(0, len(e) - 1), randint(0, 4), 1, randint(2, 10)
    print('[%d, %d, %d, %d],' % (m, n, x, y))
    e.complicate(m, n, x, y)
print(']')
print(e)
