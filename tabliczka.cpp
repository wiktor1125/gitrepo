/*
 * tabliczka.cpp
 */


#include <iostream>
#include <iomanip>


using namespace std;


void tabliczka(int x, int y){
    for (int i = 1; i <= x; i = i++) {
        for (int j = 1; j <= y; j++) {
            cout << setw(4) << i * j << " ";
            }
            count << endl;
        
        }
    
    }

int main(int argc, char **argv)
{
	
    int a, b;
    a = b = 0;
    cout << "Podaj zakres 1: ";
    cin >> a;
    
    cout << "Podaj zakre 2: ";
    cin >> b;
    tabliczka(a, b);


	return 0;
}

