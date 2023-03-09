#!/usr/bin/python3
if __name__ == "__main__":
    """print the addition and subtraction and multiplication and division of a and d """
    import calculator_1 as cal
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, cal.add(a, b)))
    print('{} - {} = {}'.format(a, b, cal.sub(a, b)))
    print('{} * {} = {}'.format(a, b, cal.mul(a, b)))
    print('{} / {} = {}'.format(a, b, cal.div(a, b)))
