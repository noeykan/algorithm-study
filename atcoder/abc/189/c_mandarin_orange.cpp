// Mandarin Orange
// https://atcoder.jp/contests/abc189/tasks/abc189_c

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int orange[10000];

int main()
{
    int n;
    cin >> n;
    
    for (int i=0; i<n; ++i) {
        cin >> orange[i];
    }
    int maxOrange = 0;
    for (int i=0; i<n; ++i) {
        int minOrange = INT_MAX;
        for (int j=i; j<n; ++j) {
            minOrange = min(minOrange, orange[j]);
            maxOrange = max(maxOrange, (j-i+1) * minOrange);
        }
    }
    cout << maxOrange;

    return 0;
}
