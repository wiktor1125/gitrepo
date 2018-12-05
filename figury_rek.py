#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  slonce.py

import turtle as t

def figura(bok, kat, ile):
    for i in range(ile):
        t.forward(bok)
        t.right(kat) 

def figura_rek(bok, kat, ile, krok):
    t.forward(bok)
    t.right(kat)
    print(ile)
    if ile > 0: 
        figura_rek(bok - krok, kat + krok, ile-1, krok)
    
def main():
    t.setup(800, 600)
    t.color('blue', 'red')
    t.begin_fill()
    t.speed(0)
    
    figura_rek(200, 60, 10, 5)
    
    t.end_fill()
    t.done()
    return 0
    
main()
