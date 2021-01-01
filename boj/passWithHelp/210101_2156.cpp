// 포도주 시식
// https://www.acmicpc.net/problem/2156
/* 하... 몇시간 생각하다 2년전에 푼 문젠데 못풀고 다시 답을 봤다 */
/*
아래와 같은 세 경우가 있으므로
oox : d[2]
oxo : d[1] + a[3]
xoo : d[0] + a[2] + a[3]
*/

#include <iostream>
#include <algorithm>

int a[10001];
int d[10001];

int f(const int n) {
    if (d[n] == -1) {
        if (n == 0) d[n] = 0;
        else if (n == 1) d[n] = a[1];
        else if (n == 2) d[n] = a[1] + a[2];
        else {
            d[n] = std::max(std::max(f(n-1), f(n-2) + a[n]),
                        f(n-3) + a[n-1] + a[n]);
        }
    }
    return d[n];
}

int main()
{
    int n;
    std::cin >> n;
    
    for (int i=1; i<=n; ++i) {
        std::cin >> a[i];
    }
    
    std::fill_n(d, n+1, -1);
    std::cout << f(n);

    return 0;
}