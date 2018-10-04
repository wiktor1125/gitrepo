#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw2.py
#  



def main(args):
    
    suma = 0
    liczba = -1
    
    while liczba !=0:
        liczba = int(input("Podaj liczbę: "))
        while liczba < 0:
            liczba = int(input("Błędne dane! Podaj liczbę:"))
        suma += liczba
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


def main2(args):
    
    suma = 0
    liczba = -1
    
    while liczba !=0:
        liczba = int(input("Podaj liczbę: "))
        if liczba < 0:
          print("Błędne dane! ", end='')
        else:
            suma += liczba
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main2(sys.argv))
