from fractions import Element, Sign


class Equation:

    def __init__(self, out=1):
        if type(out) is Element:
            self.tab = [out]
        else:
            self.tab = [Element(abs(out))]
            if out < 0:
                self.tab += ['-']

    def __len__(self):
        return len(self.indices())

    def complicate(self, m, n, x, y):
        z = Element(x, y)
        if n == 0:
            self.create_sum(m, z)
        elif n == 1:
            self.create_sub(m, z)
        elif n == 2:
            self.create_negation(m)
        elif n == 3:
            self.create_multiplication(m, z)
        elif n == 4:
            self.create_division(m, z)

    def element(self, index):
        args = self.indices()[index]
        e = self.tab
        for i in args:
            e = e[i]
        return e

    def get_triple(self, index):
        e = self.tab
        args = self.indices()[index]
        for i in range(len(args) - 1):
            index = args[i]
            e = e[index]
        index = args[-1]
        return e, index, e[index]

    def create_sum(self, index, e2):
        e, index, e0 = self.get_triple(index)
        e1 = e0 - e2
        e[index] = [e1.simplify(), e2.simplify(), '+']

    def create_sub(self, index, e2):
        e, index, e0 = self.get_triple(index)
        e1 = e0 + e2
        e[index] = [e1.simplify(), e2.simplify(), '-']

    def create_negation(self, index):
        e, i, e0 = self.get_triple(index)
        e[i] = [e0.simplify(), '-']
        if len(e) == 3:
            if e[-1] == '-':
                e[-1] = '+'
            elif e[-1] == '+':
                e[-1] = '-'
        elif len(e) == 2:
            if e is self.tab:
                e[i] = [e[i], '-']
            else:
                args = self.indices()[index]
                e = self.tab
                while len(e) != 3 and len(args) > 1:
                    args = args[:-1]
                    e = self.tab
                    for a in args:
                        e = e[a]
                if e[-1] == '+':
                    e[-1] = '-'
        elif len(e) == 1:
            e, i, e0 = self.get_triple(index)
            e[i] = [e0.simplify(), '-']

    def create_multiplication(self, index, e2):
        e, i, e0 = self.get_triple(index)
        e1 = e0 / e2
        if e1.sign is Sign.negative:
            e1 = [-e1, '-']
        if e2.sign is Sign.negative:
            e2 = [-e2, '-']
        e[i] = [e1, e2, '*']

    def create_division(self, index, e2):
        e, i, e0 = self.get_triple(index)
        e1 = e0 * e2
        e1, e2 = e1.simplify(), e2.simplify()
        if e1.sign is Sign.negative:
            e1 = [-e1, '-']
        if e2.sign is Sign.negative:
            e2 = [-e2, '-']
        e[i] = [e1, e2, ':']

    def levels(self, tab=None, i=0):
        if tab is None:
            tab = self.tab
        out = []
        if type(tab) is Element:
            return [i]
        elif type(tab) is list:
            for e in tab:
                out += self.levels(e, i + 1)
        return out

    def indices(self, tab=None, x=[]):
        if tab is None:
            tab = self.tab
        out = []
        for i in range(len(tab)):
            if type(tab[i]) is Element:
                out += [x + [i]]
            elif type(tab[i]) is list:
                out += self.indices(tab[i], x + [i])
        return out

    def operator(self, index):
        tab = self.indices()[index]
        e = self.tabo
        for i in range(len(tab) - 1):
            e = e[tab[i]]
        if tab[-1] == 1:
            return ''
        else:
            return ' ' + e[-1] + ' '

    def __str__(self):
        return self.show()

    def show(self, tab=None, usetex=False):
        if tab is None:
            if len(self.tab) == 1 and type(self.tab) is list:
                self.tab = self.tab[0]
            tab = self.tab
        if type(tab) is Element:
            if usetex:
                return tab.tex()
            else:
                return str(tab)
        else:
            if len(tab) == 0:
                return ''
            elif len(tab) == 1:
                return self.show(tab[0], usetex)
            elif len(tab) == 2:
                if tab[1] == '-':
                    if tab is self.tab:
                        return '%s' % (tab[1] + self.show(tab[0], usetex))
                    else:
                        return '(%s)' % (tab[1] + self.show(tab[0], usetex))
            else:
                s = self.show(tab[0], usetex) + ' ' + tab[2] + ' ' + self.show(tab[1], usetex)
                if tab[2] == '-' and tab is not self.tab:
                    s = '(%s)' % s
                if tab[2] == ':' and len(tab[1]) > 1:
                    s = self.show(tab[0], usetex) + ' ' + tab[2] + ' (' + self.show(tab[1], usetex) + ')'

                return s

    def tex(self):
        return self.show(None, True)
