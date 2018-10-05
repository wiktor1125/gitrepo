#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw4-pentla.py
#  


def main(args):
	
	for liczba in range(10,100):
		if liczba % 2 ==0 liczba % 3 == 0:
			print(liczba)
	
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
