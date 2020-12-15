// 합분해
// https://www.acmicpc.net/problem/2225
/* 몇시간동안 고민해도 안풀려서 결국 블로그 보고 힌트 얻어서 다시 푼 문제 ㅠㅠ
아무리 일일이 숫자 써가며 규칙 찾으려고 해봐도 안풀렸는데 이럴땐 차라리 바로
점화식 정의부터 접근해서 풀어보도록 하자 */
/*
d(n,k) = 정수 k개를 더해서 그 합이 n이 되는 경우의 수
       = d(n, k-1) + d(n-1, k-1) + ... + d(1, k-1)
d(1,1) = 1 (1)
d(1,2) = d(1,1) + d(0,1) = 1 + 1 = 2 (10, 01)
...
초기화는 d(1,1), d(0,1) 등 이런 것들만 해주면 됨
*/
#include <iostream>
#include <algorithm>

int d[201][201];

int getAns(int n, int k) {
    if (d[n][k] == -1) {
        if (k == 1) {
            d[n][k] = 1;
        } else {
            long long sum = 0;
            for (int i=0; i<=n; ++i) {
                sum += getAns(i, k-1);
            }
            d[n][k] = sum % 1000000000;
        }
    }
    return d[n][k];
}

int main()
{
    int n, k;
    std::cin >> n >> k;
    std::fill(&d[0][0], &d[200][201], -1);
    std::cout << getAns(n, k);
    return 0;
}
