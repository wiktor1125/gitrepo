/*
 * fibonacci.cpp
 */


#include <iostream>

using namespace std;

long int fibonacci_it(int n){
    
    long int a = 0; 
    long int b = 1;
    if (n == 0)
        return a;
    else if(n == 1)
        return b;
    
    
    int wynik = 0;
    for(int i = 2; i <= n; i++){
        wynik = a + b;
        a = b;
        b = wynik;
        }
        return wynik;
    }

int main(int argc, char **argv)
{
	int n = 0;
    cout << "Podaj nr wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
    cout << fibonacci_it(n);
	return 0;
}

