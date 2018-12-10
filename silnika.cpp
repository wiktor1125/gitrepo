/*
 * silnika.cpp
 */


#include <iostream>
using namespace std;

int silnia_it(int a){
    int wynik = 1;
    for (int i = 1; i < a; i++){
        wynik = a * (a - 1);
            }
        return wynik;
    }

int silnia_rek(int a){
    if (a == 1)
        return 1;
    return a * silnia_rek(a - 1);
    
    }

int main(int argc, char **argv)
{
    int a;
    cout << "podaj liczbę: ";
    cin >> a;
    cout << "Silnia: " << silnia_it(a) << endl;
    cout << "silnia: " << silnia_rek(a) << endl; 
	return 0;
}

