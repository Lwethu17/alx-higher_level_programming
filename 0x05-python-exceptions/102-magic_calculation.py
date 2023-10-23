#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0;
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            res += a ** b /n
        except Exception:
            res = b + a
            break
    return res
