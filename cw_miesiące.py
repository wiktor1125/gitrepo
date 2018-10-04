#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw_miesiące.py
#  



def main(args):
    
    
	miesiac = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
	
	while 1 > 0:
		liczba = int(input("Podaj szukany numer miesiąca: "))
		if liczba > 12 or liczba < 1:
			print("Wprowadzone dane są błędne!")
		else:
			print (miesiac[liczba - 1])

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
