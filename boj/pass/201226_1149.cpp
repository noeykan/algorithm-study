// RGB거리
// https://www.acmicpc.net/problem/1149
/*
고민 좀 하다가 생각 나서 풀었음
d[n][k] = n번째 집까지 마지막을 k로 칠했을 때 최소 비용
*/

#include <iostream>
#include <algorithm>

int p[1001][3];
int d[1001][3];

int main()
{
    int n;
    std::cin >> n;
    for (int i=1; i<=n; ++i) {
        std::cin >> p[i][0] >> p[i][1] >> p[i][2];
    }
    
    d[1][0] = p[1][0];
    d[1][1] = p[1][1];
    d[1][2] = p[1][2];
    for (int i=2; i<=n; ++i) {
        d[i][0] = std::min(d[i-1][1], d[i-1][2]) + p[i][0];
        d[i][1] = std::min(d[i-1][0], d[i-1][2]) + p[i][1];
        d[i][2] = std::min(d[i-1][0], d[i-1][1]) + p[i][2];
    }
    
    std::cout << std::min(std::min(d[n][0], d[n][1]),d[n][2]);
    return 0;
}