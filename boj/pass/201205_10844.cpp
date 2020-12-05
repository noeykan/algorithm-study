// 쉬운 계단 수
// https://www.acmicpc.net/problem/10844
/* 이 전문제에서 2차원 배열을 활용한 점화식 문제를 풀어서 비교적 쉽게 풀었음
다만 long long 문제와 지역변수 cnt를 0으로 초기화 안해줘서 2번 틀렸음 */
/*
d[n][k] : 맨 앞이 k인 n자리 계단수의 개수
1: 9
d[1][0] : 1
d[1][1]~d[1][8] : 8
d[1][9] : 1

2: 17
(01)
10 12
21 23
32 34
43 45
54 56
65 67
76 78
87 89
98 
d[2][0] : 1 = d[1][1]
d[2][1] : 2 = d[1][0] + d[1][2]
...
*/

#include <iostream>
#include <algorithm>
using namespace std;

#define DIVISOR 1000000000

long long d[101][10];

long long getCnt(int n, int k) {
    if (d[n][k] == -1) {
        if (n == 1) {
            d[n][k] = 1;
        }
        else {
            if (k == 0) {
                d[n][k] = getCnt(n-1,k+1) % DIVISOR;
            } else if (k == 9) {
                d[n][k] = getCnt(n-1,k-1) % DIVISOR;
            } else {
                d[n][k] = (getCnt(n-1,k-1) + getCnt(n-1,k+1)) % DIVISOR;
            }
        }
    }
    return d[n][k];
}

int main()
{
    fill(&d[0][0], &d[100][10], -1);
    
    int n;
    cin >> n;
    
    long long ans = 0;
    for (int i=1; i<=9; ++i) {
        ans += getCnt(n, i);
    }
    cout << ans % DIVISOR;
    
    return 0;
}