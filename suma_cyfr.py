#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#  



def main(args):
    
	liczba = int(input("Podaj liczbę: "))
	
	cyfra = list(map(int, str(liczba)))

	print ("Suma cyfr liczby wynosi: ", sum(cyfra))
	    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
