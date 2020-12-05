// 이친수
// https://www.acmicpc.net/problem/2193
/* 유형별로 문제를 풀고 있기 때문에 전에 비슷한 문제가 있어서 쉽게 풀 수 있었음
다만, 한번 틀렸는데 int도 충분할 것 같았는데 long long 을 써야 됐다.
범위를 계산하는 정확도를 길러야겠음 */
/*
b[n][k] : k가 첫자리인 n자리 이진수 개수

1: 1
1
b[1][0]: 1
b[1][1]: 1

2: 1 
10
b[2][0]: b[1][1] + b[1][0] = 1 + 1 = 2
b[2][1]: b[1][0] = 1

3: 2
101
110

*/

#include <iostream>
#include <algorithm>

using namespace std;

long long b[91][2];

long long getCnt(int n, int k) {
    if (b[n][k] == -1) {
        if (n == 1) {
            b[n][k] = 1;
        } else {
            if (k == 0) {
                b[n][k] = getCnt(n-1, 0) + getCnt(n-1, 1);
            } else {
                b[n][k] = getCnt(n-1, 0);
            }
        }
    }
    return b[n][k];
}

int main()
{
    fill(&b[0][0], &b[90][2], -1);
    
    int n;
    cin >> n;
    
    cout << getCnt(n, 1);
    
    return 0;
}