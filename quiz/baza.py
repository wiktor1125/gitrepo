#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py

import os
import csv

def czy_jest(plik):
    """ Funkcja sprawdza istnienie pliku na dysku """
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True


def dane_z_pliku(nazwa_pliku, separator=','):
    dane = []  # pusta lista na dane
    if not czy_jest(nazwa_pliku):
        return dane
    
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordĂłw do listy
    return dane
 


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
