// 연속합 2
// https://www.acmicpc.net/problem/13398
/* 이 문제 몇시간 고민하다가 결국 못풀고 답지 봄...
답지 안봤으면 생각 못했을듯 ㅠㅠ
몇번이고 냈는데 계속 틀려서 왜그런가 봤더니 초기값 설정도 잘 생각해 줘야 한다 */
/*
        10 -4  3  1  5  6 -35 12 21 -1
d[0][]  10  6  9 10 15 21 -14 12 33 32 
d[1][]  10 10 13 14 19 25  21 33 54 53
*/
#include <iostream>
#include <algorithm>
#include <climits>

int a[100000];
int d[2][100000];

int main()
{
    int N;
    std::cin >> N;

    for (int i=0; i<N; ++i) {
        std::cin >> a[i];
    }

    int maxSum = d[0][0] = d[1][0] = a[0];
    for (int i=1; i<N; ++i) {
        d[0][i] = std::max(d[0][i-1] + a[i], a[i]);
        d[1][i] = std::max(d[0][i-1], d[1][i-1] + a[i]);
        maxSum = std::max(maxSum, std::max(d[0][i], d[1][i]));
    }

    std::cout << maxSum;
    return 0;
}
