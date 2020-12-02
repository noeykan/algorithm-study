// 2xn 타일링 2
// https://www.acmicpc.net/problem/11727
/* 쉽게 풀음. 2xn 타일링 을 풀고 와서 더 쉬움 */

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int cache[1001];

int getCnt(int n) {
    if (cache[n] == 0) {
        if (n == 1) cache[n] = 1;
        else if (n == 2) cache[n] = 3;
        else {
            cache[n] = getCnt(n-1) + 2*getCnt(n-2);
        }
    }
    return cache[n];
}

int main()
{
    int n;
    cin >> n;
    cout << getCnt(n);

    return 0;
}
