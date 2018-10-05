#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw-miesiące.py
#  


def main(args):
	
	nazwy = ['styczen', 'luty', 'marzec', 'kwiecen', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
	
	
	while 1 > 0:
		numer = int(input("Podaj numer miesiąca: "))
		if 1 > numer > 12:
			print("Wprowadzone dane są błędne !")
		else:
			print(nazwy[numer - 1])
	
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
