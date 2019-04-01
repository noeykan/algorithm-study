// 1로 만들기
// https://www.acmicpc.net/problem/1463

#include <iostream>
#include <algorithm>

using namespace std;

int cache[1000001]; // KEY point !

int getMinCnt(int n)
{
    if (n <= 1)
        return 0;

    if (cache[n])
        return cache[n];

    switch (n % 6) {
    case 0:
        cache[n] = min(min(getMinCnt(n/3),getMinCnt(n/2)),getMinCnt(n-1)) + 1;
        break;
    case 2:
    case 4:
        cache[n] = min(getMinCnt(n/2),getMinCnt(n-1)) + 1;
        break;
    case 3:
        cache[n] = min(getMinCnt(n/3),getMinCnt(n-1)) + 1;
        break;
    case 1:
    case 5:
        cache[n] = getMinCnt(n-1) + 1;
        break;
    }
    return cache[n];
}

int main(void)
{
    int n; // 1<=n<=10^6
    cin >> n;

    cout << getMinCnt(n) << endl;

    return 0;
}

