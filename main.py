from fractions import Element
from equations import Equation

e = Equation()
x = e.element(-1)
e.create_sub(-1, x/2)
x = e.element(-1)
e.create_sub(-1, x/2)
print(e)
print(e.tab)
print('str:', e.getStr())