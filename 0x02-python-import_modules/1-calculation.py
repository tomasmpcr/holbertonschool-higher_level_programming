#!/usr/bin/python3
def _print(a, s, b, r):
    print("{:d} {} {:d} = {:d}".format(a, s, b, r))

if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    a = 10
    b = 5
    _print(a, "+", b, add(a, b))
    _print(a, "-", b, sub(a, b))
    _print(a, "*", b, mul(a, b))
    _print(a, "/", b, div(a, b))
