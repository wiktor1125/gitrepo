#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka.py
#  


def tabliczka():
    for i in range(1,11):
        for j in range(1,11):
            print("{:>3}".format(i * j), end='')
        print()


def main(args):
    tabliczka()
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
