#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  
 
def trojkat (a, b, c):
   
    
    if a + b > c and a + c > b and b + c > a:
        return True
        
    return False
    
    pass
    
    return

def main(args):
    assert(trojkat(3, 4, 1) == True)
    assert(trojkat(3, 4, 1) == False)
    #a = 3 
    #b = 4 
    #c = 5 
 
    #if trojkat(a, b, c):
     #   print("Da się")
    #else:
     #   print("Ni hu hu")
         
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
