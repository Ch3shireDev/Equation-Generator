from fractions import Element


class Equation:

    def __init__(self, out=1):
        self.tab = [Element(out)]

    def __len__(self):
        return len(self.getIndices())

    def getElement(self, index):
        args = self.getIndices()[index]
        e = self.tab
        for i in args:
            e = e[i]
        return e

    def create_sum(self, index, e2):
        e = self.tab
        args = self.getIndices()[index]
        for i in range(len(args) - 1):
            index = args[i]
            e = e[index]
        index = args[-1]
        e0 = e[index]
        e1 = e0 - e2
        e[index] = [e1.simplify(), e2.simplify(), '+']

    def getLevels(self):
        return self.levels(self.tab)

    def levels(self, tab, i=0):
        out = []
        if type(tab) is Element:
            return [i]
        elif type(tab) is list:
            for e in tab:
                out += self.levels(e, i + 1)
        return out

    def getIndices(self):
        return self.indices(self.tab)

    def indices(self, tab, x=[]):
        out = []
        for i in range(len(tab)):
            if type(tab[i]) is Element:
                out += [x + [i]]
            elif type(tab[i]) is list:
                out += self.indices(tab[i], x + [i])
        return out

    def getOperator(self, index):
        tab = self.getIndices()[index]
        e = self.tab
        for i in range(len(tab) - 1):
            e = e[tab[i]]
        if tab[-1] == 1:
            return ''
        else:
            return ' ' + e[-1] + ' '

    def __str__(self):
        tab = self.getIndices()
        s = ''
        i = 0
        for indices in tab:
            print(i, indices)
            s += str(self.getElement(i))
            if indices[-1] == 0:
                s += self.getOperator(i)
            i += 1

        return s
