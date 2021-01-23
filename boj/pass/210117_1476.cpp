// https://www.acmicpc.net/problem/1476
// 날짜 게산
/* 풀긴 했는데, 좀 더 깔끔하고 수학적으로 직관적인 버전을 참고하여 다시 넣어 봄
핵심은 나머지가 0부터가 아니라 1부터인 걸 어떻게 처리하냐에 달림
*/
#include <iostream>
#include <algorithm>

// 내 풀이
/*
int main()
{
    int E, S, M;
    std::cin >> E >> S >> M;

    if (E == 15) E = 0;
    if (M == 19) M = 0;

    int i = 0;
    int ans;
    while(1) {
        ans = 28 * (i++) + S;
        if (ans % 15 == E && ans % 19 == M) {
            break;
        }
    }
    std::cout << ans;
    return 0;
}
*/

// 좀더 fancy 한 버전
int main()
{
    int E, S, M;
    std::cin >> E >> S >> M;

    --E;
    --S;
    --M;

    int ans = S;
    while (true) {
        if (ans % 15 == E && ans % 19 == M) {
            break;
        }
        ans += 28;
    }
    std::cout << ans + 1;
    return 0;
}
