/*
 * liczba123.cpp

 */


#include <iostream>

using namespace std;


int liczby2() {
    int ile = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++ ) {
            if (i != j) {
                cout << i << j << " ";
                ile++;
            }
        }
    }
    return ile;
}


int liczby3() {
    int ile = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++ ) {
            for (int k = 0; k < 10; k++ ){
                if (i != j && i != k && j != k) {
                    cout << i << j << k << " ";
                    ile++;
                }
            }
        }
    }
    return ile;
}




int main(int argc, char **argv)
{
	//int ile = liczby2();
    //cout << "\n\nLiczb II cyfrowych: " << ile << endl;
    
	int ile = liczby3();
    cout << "\n\nLiczb III cyfrowych: " << ile << endl;
    
    
	return 0;
}
