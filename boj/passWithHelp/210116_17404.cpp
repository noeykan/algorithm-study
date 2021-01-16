// https://www.acmicpc.net/problem/17404
// RGB거리 2
/* 하... RGB 거리랑 문제가 같은데 조건 하나가 추가된 건데, 이걸 풀려고 몇시간을 생각했는데 결국 간단한 원리였다.
나는 1번집색깔을 계속 마지막까지 트래킹할려고 노력했었는데, 그게 아니라 그냥 처음 색깔을 고정했을 때의 경우의 수들을 먼저 구한 후,
나중에 그 중에 최소값 구하는게 씬 간단했음... 다르게 생각하면 쉽게 풀릴 문제구먼... */

#include <iostream>
#include <algorithm>

#define MAX_NUM (1000*1000 + 1)

int price[1000][3];
int sum[1000][3];

int main()
{
    int N;
    
    std::cin >> N;
    for (int i=0; i<N; ++i) {
        for (int j=0; j<3; ++j) {
            std::cin >> price[i][j];
        }
    }
    
    int ans = MAX_NUM;
    for (int i=0; i<3; ++i) { // 첫번째 집 색깔
        for (int j=0; j<3; ++j) {
            if (j == i) {
                sum[0][j] = price[0][j];
            } else {
                sum[0][j] = MAX_NUM; // MAX값임. INT_MAX로 하면 안됨.
            }
        }
        for (int j=1; j<N; ++j) {
            sum[j][0] = std::min(sum[j-1][1], sum[j-1][2]) + price[j][0];
            sum[j][1] = std::min(sum[j-1][0], sum[j-1][2]) + price[j][1];
            sum[j][2] = std::min(sum[j-1][0], sum[j-1][1]) + price[j][2];
        }
        ans = std::min(sum[N-1][(i+2)%3], std::min(ans, sum[N-1][(i+1)%3])); 
    }
    std::cout << ans;

    return 0;
}
