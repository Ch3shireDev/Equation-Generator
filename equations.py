from fractions import Element


class Equation:

    def __init__(self, out=1):
        self.tab = [Element(out)]

    def fraction(self):
        e = self.tab
        while type(e[0]) is not Element:
            e = e[0]
        e0 = e[0]
        e2 = Element(1, e0.b + 1)
        e1 = e0 - e2
        e[0] = [e1, e2, '+']
