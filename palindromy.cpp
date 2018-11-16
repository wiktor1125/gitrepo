/*
 * znaki.cpp
 */

#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char w[], int r) {
    bool pal = true;
    for (int i = 0; i < r / 2; i++) {
        if (w[i] == w[r-1-i])
            ; // instrukcja pusta
        else {
            pal=false;
            break;
        }
    }
    return pal;
}

int main(int argc, char **argv)
{
    int roz = 20;
    char wyraz[roz]; 
    cout << "Podaj wyraz:\n";
    cin.getline(wyraz, roz);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
    return 0;
}
