from fractions import Element, gcd


class Class:
    def __init__(self, *args, **kwargs):
        for x in args:
            print(x)


if __name__ == '__main__':
    print(Element(-1, 2))
    # print(gcd(12,18))