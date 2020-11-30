// 진법 변환 2
// https://www.acmicpc.net/problem/11005
/* 쉽게 풀었음 */

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    char num2char[36];
    for (int i=0; i<36; ++i) {
        if (i <= 9)
            num2char[i] = '0' + i;
        else
            num2char[i] = 'A' + (i-10);
    }
    
    int n, base;
    cin >> n >> base;
    
    string ans;
    while (n != 0) {
        ans += num2char[n % base];
        n = n/base;
    }
    
    reverse(ans.begin(), ans.end());
    
    cout << ans;
    
    return 0;
}
