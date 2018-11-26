#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
from peewee import *

baza_plik = 'test_orm.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Uczen(BazaModel):
    
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    egz_hum = DecimalField(default=0)
    egz_mat = DecimalField(default=0)
    egz_jez = DecimalField(default=0)
    klasa = ForeignKeyField(Klasa, related_name='id_klasa')



class Przedmiot(BazaModel):
    
    przedmiot= CharField(null=False)
    imie_naucz=CharField(null=False)
    nazwisko_naucz=CharField(null=False)
    plec_naucz=BooleanField()
    
class Ocena(BazaModel):
    
    datad= DateField()
    ocena= DecimalField()
    uczen = ForeignKeyField(Uczen, related_name='id_uczen')
    przedmiot = ForeignKeyField(Przedmiot, related_name='id_przedmiot')
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Uczen, Klasa, Ocena, Przedmiot])
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.imie, uczen.nazwisko)
        
    klasy = Klasa.select()
    for 
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
