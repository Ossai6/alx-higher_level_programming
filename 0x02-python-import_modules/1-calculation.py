#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, mul, div
    a = 10
    b = 5

    _sum = add(a, b)
    _sub = sub(a, b)
    _mul = mul(a, b)
    _div = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, _sum))
    print("{:d} - {:d} = {:d}".format(a, b, _sub))
    print("{:d} * {:d} = {:d}".format(a, b, _mul))
    print("{:d} / {:d} = {:d}".format(a, b, _div))
