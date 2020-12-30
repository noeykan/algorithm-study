// 스티커
// https://www.acmicpc.net/problem/9465
/* 한시간 이상 생각했는데 몰라서 결국 블로그 풀이 봄
점화식의 정의가 중요하고, n-1항과 n항이 어떻게 일반화 하여 연결되는 지가 포인트
1부터 생각하기 어려울 땐 아예 n부터 생각해보자
*/
/*
d[n][i] : n번째 줄의 i번째 까지 얻을 수 있는 최고의 점수
d[0][i] = max(d[1][i-1], d[1][i-2]) + a[0][i]
d[1][i] = max(d[0][i-1], d[0][i-2]) + a[1][i]
*/
#include <iostream>
#include <algorithm>

int a[2][100001];
int d[2][100001];

int main()
{
    int nCase;
    std::cin >> nCase;
    while (nCase--) {
        int n;
        std::cin >> n;
        
        std::fill(&a[0][0], &a[1][100001], 0);
        std::fill(&d[0][0], &d[1][100001], 0);
        for (int i=0; i<2; ++i) {
            for (int j=1; j<=n; ++j) {
                std::cin >> a[i][j];
            }
        }

        d[0][1] = a[0][1];
        d[1][1] = a[1][1];
        for (int i=2; i<=n; ++i) {
            d[0][i] = std::max(d[1][i-1], d[1][i-2]) + a[0][i];
            d[1][i] = std::max(d[0][i-1], d[0][i-2]) + a[1][i];
        }
        std::cout << std::max(d[0][n], d[1][n]) << '\n';
    }
    return 0;
}