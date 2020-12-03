// 카드 구매하기 2
// https://www.acmicpc.net/problem/16194
/*  */

#include <iostream>
#include <algorithm>

using namespace std;

// 1. 원래 내가 풀던 방식 (recursive, top-down)
/*
int p[1001];
int minP[1001];

int getMinP(int n) {
    if (minP[n] == 0) {
        if (n == 1) minP[n] = p[n];
        else {
            int candidate = p[n];
            for (int i=n-1; i>=n/2; --i) {
                candidate = min(candidate, getMinP(i)+getMinP(n-i));
            }
            minP[n] = candidate;
        }
    }
    return minP[n];
}
*/

// 2. 낮은 수부터 계산해나가는 방식 (for-loop, bottom-up)
/*
int p[1001];
int minP[1001];

int getMinP(int n) {
    minP[1] = p[1];
    for (int i=2; i<=n; ++i) {
        int candidate = p[i];
        for (int j=i-1; j>=i/2; --j) {
            candidate = min(candidate, minP[j] + minP[i-j]);
        }
        minP[i] = candidate;
    }
    return minP[n];
}

int main()
{
    int n;
    cin >> n;
    for (int i=1; i<=n; ++i ) {
        cin >> p[i];
    }
    cout << getMinP(n);

    return 0;
}
*/

// 3. 배열 변수 하나 안쓰고도 input 입력 하면서 바로 계산 (bottom-up)
int minP[1001];

int main()
{
    int n, p;
    cin >> n;
    cin >> minP[1];

    for (int i=2; i<=n; ++i ) {
        cin >> p;
        for (int j=i-1; j>=i/2; --j) {
            p = min(p, minP[j]+minP[i-j]);
        }
        minP[i] = p;
    }
    cout << minP[n];

    return 0;
}