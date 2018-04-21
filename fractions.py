from math import ceil, sqrt
from enum import Enum


def gcd(a, b):
    a, b = abs(a), abs(b)
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def divisors(b):
    print(b)
    b = abs(b)
    if b < 2:
        return [1]
    div = []
    while b != 1:
        for i in range(2, b + 1):
            if b % i == 0:
                div += [i]
                b //= i
                break
    return list(set(div + [1, b]))


def is_prime(b):
    b = abs(b)
    for i in range(2, ceil(sqrt(b))):
        if b % i == 0:
            return False
    return True


class Sign(Enum):
    positive = True
    negative = False


class Element:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.a, self.b = args
            self.sign = Sign.positive
        elif len(args) == 3:
            self.a, self.b, self.sign = args
        if (self.a < 0) != (self.b < 0):
            if self.sign == Sign.positive:
                self.sign = Sign.negative
            else:
                self.sign = Sign.positive
        self.a, self.b = abs(self.a), abs(self.b)

    def __str__(self):
        a, b = self.a, self.b
        if a == 0:
            return '0'
        s = ''
        if self.sign == Sign.negative:
            s += '-'
        if a // b != 0:
            s += '%d' % (a // b)
        if b == 10 or b == 100 or b == 1000:
            if a % b > 0:
                s += '%d.%d' % (a // b, a % b)
            else:
                s += '%d' % (a // b)
        elif a % b != 0:
            s += '\\frac{%d}{%d}' % (a % b, b)
        return s

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self.sign == other.sign:
            a = self.a * other.b + self.b * other.a
        else:
            a = self.a * other.b - self.b * other.a
        b = self.b * other.b
        sign = self.sign
        if a < 0 and sign is sign.negative:
            a = abs(a)
            sign = sign.positive
        return Element(a, b, sign)

    def __neg__(self):
        if self.sign is Sign.positive:
            sign = Sign.negative
        else:
            sign = Sign.positive
        return Element(self.a, self.b, sign)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        if self.a == 0 and other.a == 0:
            return True

        e1 = self.simplify()
        e2 = other.simplify()

        if e1.a == e2.a and e1.b == e2.b and e1.sign == e2.sign:
            return True
        else:
            return False

    def simplify(self):
        c = 2
        a, b = self.a, self.b
        while c > 1:
            c = gcd(a, b)
            a //= c
            b //= c
        return Element(a, b, self.sign)
