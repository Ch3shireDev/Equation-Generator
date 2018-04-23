from fractions import Element, Sign
from equations import Equation
import unittest


class Test(unittest.TestCase):
    def test_str(self):
        x = Element(1, 2)
        s = str(x)
        self.assertEqual(s, '1/2')

    def test_add(self):
        x, y = Element(1, 2), Element(1, 3)
        z = x + y
        self.assertEqual(z.a, 5)
        self.assertEqual(z.b, 6)

    def test_negate(self):
        x, y = Element(1, 2, Sign.positive), Element(1, 2, Sign.negative)
        self.assertEqual(str(-x), '-1/2')
        self.assertEqual(str(-y), '1/2')
        self.assertEqual(str(-(-x)), '1/2')

    def test_subtract(self):
        self.assertEqual(str(Element(1, 2) - Element(1, 3)), '1/6')
        self.assertEqual(str(Element(1, 3) - Element(1, 2)), '-1/6')

    def test_equal(self):
        self.assertEqual(Element(1, 2), Element(1, 2))
        self.assertEqual(Element(0, 2), Element(0, 3))
        self.assertEqual(Element(0, 2), -Element(0, 3))
        self.assertEqual(Element(1, 2), Element(2, 4))
        self.assertEqual(Element(-1, 2), -Element(1, 2))

    def test_parse(self):
        self.assertEqual(Element('1/2'), Element(1, 2))
        self.assertEqual(Element('-1/2'), -Element(1, 2))
        self.assertEqual(Element('3'), Element(3, 1))
        self.assertEqual(Element('-3'), -Element(3, 1))
        self.assertEqual(Element('0.5'), Element(1, 2))
        self.assertEqual(Element('1.5'), Element(3, 2))

    def test_multiply(self):
        self.assertEqual(Element('2/3') * Element('5/7'), Element('10/21'))

    def test_division(self):
        self.assertEqual(Element('2/3') / Element('5/7'), Element('14/15'))

    def test_sum_equation(self):
        e = Equation()
        for i in range(5):
            x = e.element(-1)
            e.create_sum(-1, x / 2)
        s = str(e)
        self.assertEqual(s, '1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/32')

    def test_sub_equation(self):
        e = Equation()
        x = e.element(-1)
        e.create_sub(-1, x / 2)
        self.assertEqual(str(e), '1 1/2 - 1/2')
        x = e.element(-1)
        e.create_sub(-1, x / 2)
        self.assertEqual(str(e), '1 1/2 - (3/4 - 1/4)')
        x = e.element(-1)
        e.create_sub(-1, x / 2)
        self.assertEqual(str(e), '1 1/2 - (3/4 - (3/8 - 1/8))')


if __name__ == '__main__':
    unittest.main()
