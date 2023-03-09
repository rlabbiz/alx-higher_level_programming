#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print('{} + {} = {}'.format(a, b, cal.add(a, b)))
    print('{} - {} = {}'.format(a, b, cal.sub(a, b)))
    print('{} * {} = {}'.format(a, b, cal.mul(a, b)))
    print('{} / {} = {}'.format(a, b, cal.div(a, b)))
