from fractions import Element
from equations import Equation
from random import randint

print(r'\documentclass[8pt]{article}')
print(r'\usepackage[utf8]{inputenc}')
print(r'\usepackage{polski}')
print(r'\usepackage{amsmath}')
print(r'\begin{document}')

N = 15

for _ in range(100):
    print(r'\begin{align}')
    for i in range(N):
        e = Equation()
        # print('[')
        for j in range(5):
            m, n, x, y = randint(0, len(e) - 1), randint(0, 4), 1, randint(2, 10)
            e.complicate(m, n, x, y)
        if i < N - 1:
            print(e.tex(), r'\\')
        else:
            print(e.tex())
    print(r'\end{align}')

print(r'\end{document}')
