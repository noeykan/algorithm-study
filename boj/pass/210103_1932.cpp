// 정수 삼각형
// https://www.acmicpc.net/problem/1932
/* 풀었는데, 좀 더 효율적인 코드 찾아보고 추가로 덧붙임
메모리가 획기적으로 줄고, 시간도 더 줄어서 효율적임
i=1부터 증가하는 식이 아니라 i=n 부터 감소하는 식으로 하니까, table 하나로 커버할 수 있게 됨
더불에 max_element 라는 함수도 알게됨 */

#include <iostream>
#include <algorithm>

#define NUM 500

// 내 풀이
/*
int a[NUM+1][NUM+1];
int d[NUM+1][NUM+1];

int main()
{
    int n;
    std::cin >> n;
    
    for (int i=1; i<=n; ++i) {
        for (int j=1; j<=i; ++j) {
            std::cin >> a[i][j];
        }
    }
    
    for (int i=1; i<=n; ++i) {
        for (int j=1; j<=i; ++j) {
            d[i][j] = std::max(d[i-1][j-1], d[i-1][j]) + a[i][j];
        }
    }
    
    int maxSum = 0;
    for (int j=1; j<=n; ++j) {
        if (maxSum < d[n][j])
            maxSum = d[n][j];
    }
    
    std::cout << maxSum;

    return 0;
}
*/

// 다른 사람 코드 참고
int d[NUM+1];

int main()
{
    int N, n;
    std::cin >> N;
    
    for (int i=1; i<=N; ++i) {
        // j=i부터 거꾸로 하게 되면, d를 1차원 배열로 할 수 있음
        for (int j=i; j>=1; --j) {
            std::cin >> n;
            d[j] = std::max(d[j], d[j-1]) + n;
        }
    }
    
    std::cout << *std::max_element(d+1, d+NUM+1);
    return 0;
}