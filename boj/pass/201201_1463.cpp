// 1로 만들기
// https://www.acmicpc.net/problem/1463
/* 전에 풀었던 문제인데 다시 풀기 도전해서 바로 풀었음
전에 풀었던 풀이보다 더 깔끔해서 맘에 듦 */

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int minCnt[1000001];

int getMinCnt(int n) {
    if (minCnt[n] == 0) {
        if (n == 1) {
            minCnt[n] = 0;
        } else if (n == 2 || n == 3) {
            minCnt[n] = 1;
        } else {
            int minNum = INT_MAX;
            if (n % 3 == 0) {
                minNum = min(minNum, getMinCnt(n/3));
            }
            if (n % 2 == 0) {
                minNum = min(minNum, getMinCnt(n/2));
            }
            minCnt[n] = min(minNum, getMinCnt(n-1)) + 1;
        }
    }
    return minCnt[n];
}

int main()
{
    int input;
    cin >> input;
    
    cout << getMinCnt(input);

    return 0;
}
