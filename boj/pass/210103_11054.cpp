// 가장 긴 바이토닉 부분 수열
// https://www.acmicpc.net/problem/11054
/* 몇시간 동안 고민하다가 겨우 품
초기화 값(ans)을 0으로 해서 처음에 틀렸는데 나중에 1로 해서 알아냄 */

#include <iostream>
#include <algorithm>

int a[1000];
int d[2][1000];

int main()
{
    int N;
    std::cin >> N;
    for (int i=0; i<N; ++i) {
        std::cin >> a[i];
    }

    int ans = 1;
    std::fill(&d[0][0], &d[1][1000], 1);
    for (int i=0; i<N; ++i) {
        for (int j=0; j<i; ++j) {
            if (a[j] < a[i]) {
                d[0][i] = std::max(d[0][i], d[0][j] + 1);
                ans = std::max(d[0][i], ans);
            }
            else if (a[j] > a[i]) {
                d[1][i] = std::max(std::max(d[1][i], d[1][j] + 1), d[0][j] + 1); 
                ans = std::max(d[1][i], ans);
            }
        }
    }

    std::cout << ans;
    return 0;
}