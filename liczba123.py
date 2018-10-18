#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczba123.py
#  

def liczby2():
    
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe, 
    w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 11, 22, 33 itd.
    """
    ile = 0
    for i in range(1,10):
        for j in range(0,10):
            if i != j: 
                print("{}{} ".format(i,j), end='')
                ile = ile + 1
    return ile

    """
    Funkcja drukuje wszystkie liczby trzycyfrowe, 
    w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 112, 224, 333 itd.
    """ 
def liczby3():

    ile = 0
    for s in range(1,10):
        for d in range(0,10):
            for j in range(0,10):
                if s != d and s != j and d != j:
                    print("{}{}{} ".format(s,d,j), end='')
                    ile = ile + 1
    return ile


def main(args):
    print("\n\nLiczb 2-cyfrowych: ", liczby2())
    print("\n\nLiczb 3-cyfrowych: ", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
