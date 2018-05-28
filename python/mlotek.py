#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby
    print("wylosowano:", liczba)
    # pobieranie danych od użytkownika
    for i in range(3):
        print("Próba", i + 1)
        odp = input("Podaj liczbe od 1 do 10:")
        print("liczba", odp)

        if liczba == int(odp):  # porównanie odp z wylosowaną liczbą
            print("Zgadłeś!")
            break  # przerwanie działania pętli
        elif i == 2:
            print("Wylosowano", liczba)
        else:
            print("Spróbuj ponownie")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
