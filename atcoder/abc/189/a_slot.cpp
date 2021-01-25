// Slot
// https://atcoder.jp/contests/abc189/tasks/abc189_a

#include <iostream>

using namespace std;

int main()
{
    char c[3];
    cin >> c[0] >> c[1] >> c[2];
    
    if (c[0] == c[1] && c[1] == c[2])
        cout << "Won";
    else
        cout << "Lost";
    return 0;
}