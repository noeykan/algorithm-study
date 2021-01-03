// 가장 큰 증가 부분 수열
// https://www.acmicpc.net/problem/11055
/* 전에 이런 비슷한 문제를 풀어봐서 쉽게 풀음
다 풀고 나서 다른 사람 코드를 참고했는데,
max를 구할 때 나처럼 max=0 를 하고 if (max < x) max = x 이렇게 하는 것 보다,
max = std::max(max, x) 이렇게 하는게 더 코드상 깔끔한 것 같으니 손에 익도록 해 두자 */

#include <iostream>
#include <algorithm>

int a[1000];
int d[1000];

int main()
{
    int N;
    std::cin >> N;
    
    for (int i=0; i<N; ++i) {
        std::cin >> a[i];
    }

    int ans = 0;
    for (int i=0; i<N; ++i) {
        d[i] = a[i];
        for (int j=0; j<i; ++j) {
            if (a[j] < a[i]) {
                d[i] = std::max(d[i], d[j] + a[i]);
            }
        }
        ans = std::max(ans, d[i]);
    }
    
    std::cout << ans;
    
    return 0;
}