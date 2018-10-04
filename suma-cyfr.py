#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  


def main(args):
    
    liczba = input("Podaj liczbę 2-cyfrową: ")
    liczba = int(liczba)
    
    while liczba < 10:
        liczba = input("Podaj liczbę 2-cyfrową: ")
        liczba = int(liczba)
 
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba/ 10)
        
    print("Suma:", suma)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
