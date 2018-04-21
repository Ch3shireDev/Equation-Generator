from fractions import Element, Sign
import unittest


class Test(unittest.TestCase):
    def test_str(self):
        x = Element(1, 2)
        s = x.__str__()
        self.assertEqual(s, '\\frac{1}{2}')

    def test_add(self):
        x, y = Element(1, 2), Element(1, 3)
        z = x + y
        self.assertEqual(z.a, 5)
        self.assertEqual(z.b, 6)

    def test_negate(self):
        x, y = Element(1, 2, Sign.positive), Element(1, 2, Sign.negative)
        self.assertEqual(str(-x), '-\\frac{1}{2}')
        self.assertEqual(str(-y), '\\frac{1}{2}')
        self.assertEqual(str(-(-x)), '\\frac{1}{2}')

    def test_subtract(self):
        self.assertEqual(str(Element(1, 2) - Element(1, 3)), '\\frac{1}{6}')
        self.assertEqual(str(Element(1, 3) - Element(1, 2)), '-\\frac{1}{6}')

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


if __name__ == '__main__':
    unittest.main()
