// 진법 변환
// https://www.acmicpc.net/problem/2745
/* 쉽게 풀었음 */

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int base;
    int ans = 0;
    string n;
    cin >> n >> base;
    
    reverse(n.begin(), n.end());
    for (int i=0; i<n.size(); ++i) {
        if (n[i] >= '0' && n[i] <= '9') {
            ans += (n[i]-'0')*pow(base, i);
        } else if (n[i] >= 'A' && n[i] <= 'Z') {
            ans += (n[i]-'A'+10)*pow(base, i);
        }
    }

    cout << ans;

    return 0;
}
