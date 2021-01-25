// Logical Expression
// https://atcoder.jp/contests/abc189/tasks/abc189_d

#include <iostream>
using namespace std;

bool op[61];
int x[61][2]; // [][0]: True, [][1]: False
int y[61][2];

int main()
{
    int n;
    cin >> n;
    for (int i=1; i<=n; ++i) {
        string in;
        cin >> in;
        if (in == "AND") op[i] = true;
        else op[i] = false;
    }
    
    x[0][0] = x[0][1] = y[0][0] = y[0][1] = 1;
    for (int i=1; i<=n; ++i) {
        x[i][0] = x[i][1] = x[i-1][0] + x[i-1][1];
        if (op[i]) {
            y[i][0] = x[i-1][0];
            x[i][1] = x[i-1][0] + 2*x[i-1][1];
        } else {
            d[i][0] = 2*d[i-1][0] + d[i-1][1];
            d[i][1] = d[i-1][1];
        }
    }
    cout << d[n][0];
    return 0;
}
