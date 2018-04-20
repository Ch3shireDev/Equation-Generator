from random import randint
from math import ceil, sqrt
from enum import Enum

def divisors(b):
    print(b)
    b = abs(b)
    if b < 2:return [1]
    div = []
    while b != 1:
        for i in range(2,b+1):
            if b%i == 0:
                div += [i]
                b //= i
                break
    return list(set(div+[1,b]))

class sign(Enum):
    positive = True
    negative = False

class element:
    def __init__(self, a, b, sign=sign.positive):
        self.a = abs(a)
        self.b = abs(b)
        self.sign = sign

    def is_prime(self):
        b = abs(self.b)
        for i in range(2,ceil(sqrt(b))):
            if b%i == 0:
                return False
        return True

    def __str__(self):
        a, b= self.a, self.b
        if a==0:
            return '0'
        str = ''
        if self.sign == sign.negative:
            str += '-'
        if a//b != 0:
           str += '%d' % (a//b)
        if b == 10 or b == 100 or b == 1000:
            if a%b > 0:
                str += '%d.%d' % (a//b, a%b)
            else:
                str += '%d' % (a//b)
        elif a%b != 0:
            str += '\\frac{%d}{%d}' % (a%b,b)
        return str
        
    def __add__(self, other):
        if self.sign == other.sign:
            a = self.a*other.b + self.b*other.a
        else:
            a = self.a*other.b - self.b*other.a
        b = self.b*other.b
        sign = self.sign
        if a < 0 and sign is sign.negative:
            a = abs(a)
            sign = sign.positive
        return element(a,b,sign)

def tests():
    x = element(1,2)
    if x.__str__() == '\\frac{1}{2}':
        print('pass')
    else:
        print('error')

    x, y = element(1,2), element(1,3)
    z = x + y
    if z.a == 5 and z.b == 6:
        print('pass')
    else:
        print('error')

tests()