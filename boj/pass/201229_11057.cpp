// 오르막 수
// https://www.acmicpc.net/problem/11057
/* 고민하다가 방법을 알고 간단하게 푼 문제. 다른 풀이가 있을 지 찾아봐야 겠다 */
/*
N:1 => 10
0 - 1
1 - 1
2 - 1
...
8 - 1
9 - 1

N:2 => 55
00~09 - 10
11~19 - 9
22~29 - 8
...
88~89 - 2
99~99 - 1

*/

#include <iostream>
#define MOD 10007

int cnt[10];

int main()
{
    int n;
    std::cin >> n;
    
    // n이 1인 경우 초기화
    std::fill_n(cnt, 10, 1);
    
    while (--n) {
        // cnt[9]는 항상 1이므로 계산 안함
        for (int j=8; j>=0; --j) {
            cnt[j] += cnt[j+1];
            cnt[j] %= MOD;
        }
    }
    
    int ans = 0;
    for (int i=0; i<10; ++i) {
        ans += cnt[i];
        ans %= MOD;
    }
    std::cout << ans % MOD;
    
    return 0;
}