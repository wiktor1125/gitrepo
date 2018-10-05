#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuje wypełniony prostokąt o bokach długości podanej przez użytkownika za pomocą podanego znaku  

def prostokat1(a, b, c):
    for i in range(a):
        for j in range(b):
            print(c, end='')
        print()
    
def prostokat2(a, b, c):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()

def choinka(h, c):
    for i in range(h):
        for j in range(i + 1):
            print(c, end='')
        print()
        
        
def choinka2(h, znak):
    for i in range(h):
        for j in range(h - i):
            print(znak, end='')
        print()
                    
        
        
        
def main(args):
    a = int(input('Wysokość prostokąta: '))
    b = int(input('Długość prostokąta: '))
    c = input('Wypełnienie: ')
    h = int(input('Wysokość choinki: ')) 
    
    prostokat1(a, b, c)
    print()
    prostokat2(a, b, c)
    print()
    choinka(h, c)
    print()
    choinka2(h, znak)
    print()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
