// 동물원
// https://www.acmicpc.net/problem/1309
// 잘 풀긴 했는데, 점화식 버전 풀이를 보고 이해 안되서 이해 해 보려다 몇시간을 썼네...
/*
1. dp 버전
d[n][k] : n개이고 상황이 k일때(0: 없을때, 1:왼쪽에 사자, 2:오른쪽에 사자) 경우의 수
   X 1 2
1: 1 1 1
2: 3 2 2

2. 점화식 버전
d[n] = d[n-1]*2 + d[n-2]
d[n] = d[n][0] + d[n][1] + d[n][2]
d[n][0] = d[n-1][0] + d[n-1][1] + d[n-1][2]
d[n][1] = d[n-1][0] + d[n-1][2]
d[n][2] = d[n-1][0] + d[n-1][1]

d[n] = d[n-1] + d[n-1] + d[n-1][0]
       = d[n-1] * 2 + d[n-2]

결국 d[n-1][0]이 d[n-2]와 같다는 것이 포인트이다.
n-1 칸에 아무것도 없을때의 경우의 수는 n-2 칸까지의 모든 경우의 수와 같다.
*/

// 처음 푼 버전: 메모리 3188 KB
/*
#include <iostream>
int d[100001][3];

int main()
{
    int n;
    std::cin >> n;
    
    d[1][0] = d[1][1] = d[1][2] = 1;
    for (int i=2; i<=n; ++i) {
        d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % 9901;
        d[i][1] = (d[i-1][0] + d[i-1][2]) % 9901;
        d[i][2] = (d[i-1][0] + d[i-1][1]) % 9901;
    }

    std::cout << (d[n][0] + d[n][1] + d[n][2]) % 9901;
    return 0;
}
*/

// 메모리 덜 쓰는 버전
#include <iostream>
#define MOD_NUM 9901

int d[3];
int c[3];

int main()
{
    int n;
    std::cin >> n;
    
    d[0] = d[1] = d[2] = 1;
    for (int i=2; i<=n; ++i) {
        c[0] = (d[0] + d[1] + d[2]) % MOD_NUM;
        c[1] = (d[0] + d[2]) % MOD_NUM;
        c[2] = (d[0] + d[1]) % MOD_NUM;
        d[0] = c[0];
        d[1] = c[1];
        d[2] = c[2];
    }
    std::cout << (d[0] + d[1] + d[2]) % MOD_NUM;
    return 0;
}