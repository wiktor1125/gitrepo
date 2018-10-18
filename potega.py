#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  Obliczanie potęgi liczby naturalnej 

def potega_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a
    return wynik
    


def main(args):
    a, n = 0, 2
    print("Podstawa {} do potegi {} wynosi {}".
        format(a, n, potega_it(a, n)))
    potega_it(a, n)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
