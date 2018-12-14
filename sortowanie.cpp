/*
 * sortowanie.cpp
 * 
 */


#include <iostream>
#include <cstdlib>
using namespace std;

void wypelnij(int tab[], int rozmiar) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for(int i=0; i < rozmiar; i++) {
        // cout << rand() << endl;
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar) {
    for(int i=0; i < rozmiar; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void zamien1(int &a, int &b) {
    // cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    // cout << a << " " << b << endl;
    }

void zamien2(int tab[], int i) {
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
}

void sort_bubble(int tab[], int n) {
    cout << "\nSortowanie bąbelkowe\n";
    int licznik = 0;
    for (int j = n - 1; j > 0 ; j--) {
        for(int i = 0; i < j; i++) {
            licznik++;
            if (tab[i] > tab[i+1])
                //zamien(tab[i], tab[i+1]);
                zamien2(tab, i);
        }
    }
    cout << "\nPowtórzeń: " << licznik << endl;
}


//void sort_bubble(int tab[], int n){
 //   for(int j = n - 1; j > 0; j--){
 //      for(int i = 0; i < j; i++) {
//          if (tab[i] > tab[i + 1])
 //           zamien1(tab[i], tab[i+1]);
 //          }     
//        }
 //   }


void sort_insert(int tab[], int n) {
    cout << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    for (i = 1; i < n; i++) { // pętla wybiera kolejne elementy zaczynając od drugiego
        tmp = tab[i];
        j = i - 1; // 0
        while (j >= 0 && tab[j] > tmp) {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}


int main(int argc, char **argv)
{
    int roz = 20;
    int tab[roz];
	wypelnij(tab, roz);
    drukuj(tab, roz);
    cout << endl;
    sort_bubble(tab, roz);
    drukuj(tab, roz);
    //~tab[0] = 7;
    //~tab[1] = 5;
    //~zamien1(tab[0], tab[1]);
    //~cout << tab[0] << " " << tab[1];
    return 0;
}
