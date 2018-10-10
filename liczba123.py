#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczba123.py
#  


def liczby2():
    for i in range(1,10):
        for j in range(0,10):
            if i !=j:
                print("{}{} ".format(i, j), end='')
                    ile = ile +1
        return ile
        print()




def main(args):
    print("Liczba 2 - cyfrowych: ", liczby2())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
