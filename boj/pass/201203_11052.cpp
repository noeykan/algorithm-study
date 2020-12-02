// 카드 구매하기
// https://www.acmicpc.net/problem/11052
/* 푸는 데 생각보다 오래 걸린 문제.. 풀이는 간단해 보여도 거의 1시간 고민하고 품 */
/*
(5, 2, 8, 10)
f(1) = P1 = 5
f(2) = max(P1+P1, P2) = 10
f(3) = max(P1+P1+P1, P1+P2, P3) = 15
     = max(f(2) + f(1), P3)
f(4) = max(P1+P1+P1+P1, P1+P1+P2, P2+P2, P1+P3, P4)
     = max(f(3) + f(1), f(2) + f(2), P4)

f(1)
1
f(2)
1+1
2
f(3)
1+ 1+1
1+ 2
3
f(4)
1+ 1+1+1
1+ 1+2
1+ 3
2+2
4
f(5)
1+ 1+1+1+1
1+ 1+1+2
1+ 1+3
1+ 2+2
1+ 4
2+3
5
F(6)
1+ 1+1+1+1+1
1+ 1+1+1+2
1+ 1+1+3
1+ 1+2+2
1+ 1+4
1+ 2+3
1+ 5
2+ 2+2
2+ 4
3+ 3
6
*/

#include <iostream>
#include <algorithm>

using namespace std;

int p[10001];
int maxPrice[10001];

int getMaxPrice(int n) {
    if (maxPrice[n] == 0) {
        int candidate = p[n];
        for (int i=n-1; i>=n/2; --i) {
            candidate = max(candidate, getMaxPrice(i)+p[n-i]);
        }
        maxPrice[n] = candidate;
    }
    return maxPrice[n];
}

int main()
{
    int n;
    cin >> n;
    
    for (int i=1; i<=n; ++i) {
        cin >> p[i];
    }
    
    cout << getMaxPrice(n);

    return 0;
}
