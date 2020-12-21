// 연속합
// https://www.acmicpc.net/problem/1912
/*
허무하다.. 몇시간 동안 생각해도 안풀리더니, 아프고 나서 1주 뒤에 다시 풀기 시작했는데
너무 쉽게 풀림 ㅠㅠ
*/

#include <iostream>
#include <algorithm>
#include <climits>

int s[1000001];
int sum[1000001];
int main()
{
    int n;
    int maxSum = INT_MIN;
    std::cin >> n;
    for (int i=0; i<n; ++i) {
        std::cin >> s[i];
        if (i == 0)
            sum[i] = s[i];
        else {
            sum[i] = std::max(s[i], sum[i-1] + s[i]);
        }
        if (sum[i] > maxSum) {
            maxSum = sum[i];
        }
    }
    std::cout << maxSum;
    return 0;
}