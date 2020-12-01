// 2xn 타일링
// https://www.acmicpc.net/problem/11726
/* 전에 풀었던 문제인데 다시 풀기 도전해서 바로 풀었음
전에 풀었던 풀이보다 더 깔끔해서 맘에 듦 */

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int cache[1001];

int getCnt(int n) {
    if (cache[n] == 0) {
        if (n == 1)
            cache[n] = 1;
        else if (n == 2)
            cache[n] = 2;
        else {
            cache[n] = (getCnt(n-1) + getCnt(n-2)) % 10007;
        }
    }
    return cache[n];
}

int main()
{
    int n;
    cin >> n;
    
    cout << getCnt(n);

    return 0;
}
