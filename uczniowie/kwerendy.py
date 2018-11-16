#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3

def kwerenda(cur):
    cur.execute("""
        WITH srednie AS (
        SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie
        INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, FROM srednie
        WHERE sred > 3.5 ORDER BY sred DESC
    """)
    
    #SELECT imie, nazwisko, klasa FROM uczniowie
    #INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
    #WHERE klasa='2A'
    
    wyniki = cur.fetchall()
    #LIMIT 5 
    #ORDER BY nazwisko DESC/ASC
    #WHERE plec=1
    #SELECT COUNT(ID)* FROM uczniowie
    #WHERE nazwisko LIKE '%a'
    #SELECT id FROM uczniowie
    for row in wyniki:
        print(row)



def main(args):
     # KONFIGURACJA #######
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()
    con,close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
