// 가장 긴 감소하는 부분 수열
// https://www.acmicpc.net/problem/11722
/* 바로 전에 가장 긴 증가하는 부분 수열 풀어서 쉽게 풀음 */
/*
d[n][k] = 수열이 n개 일 때 마지막이 k인 가장 긴 감소하는하는 부분 수열 길이

d[n][k] = min(d[n-1][1],...,d[n-1][k-1]) + 1
*/

int d[1001];

#include <iostream>

using namespace std;

int main()
{
    int n, a;
    cin >> n;
    
    int ans = 0;
    while (n--) {
        int maxCnt = 0;
        cin >> a;
        for (int i=1000; i>a; --i) {
            if (d[i] > maxCnt)
                maxCnt = d[i];
        }
        d[a] = maxCnt + 1;
        if (d[a] > ans)
            ans = d[a];
    }
    cout << ans;
    
    return 0;
}