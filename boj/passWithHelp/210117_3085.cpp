// https://www.acmicpc.net/problem/3085
// 사탕 게임
/* 문제 유형을 알고 풀지 않았으면 DFS 같은걸로 더 헤맬뻔 했다. 사실 브루트포스가 은근 어려운 것 같다.
노가다도 효율적으로 해야하는데 코드 짜면서도 이게 맞나 확신이 안들어서 자꾸 답 보게 된다..;
*/
#include <iostream>
#include <algorithm>

char a[51][51];
int maxCnt = 1;
int N;

void getMaxRow(int row) {
    int curCnt = 1;
    for (int j=1; j<N; ++j) {
        if (a[row][j] == a[row][j+1]) {
            curCnt++;
            if (curCnt > maxCnt)
                maxCnt = curCnt;
        } else {
            curCnt = 1;
        }
    }
}

void getMaxCol(int col) {
    int curCnt = 1;
    for (int i=1; i<N; ++i) {
        if (a[i][col] == a[i+1][col]) {
            curCnt++;
            if (curCnt > maxCnt)
                maxCnt = curCnt;
        } else {
            curCnt = 1;
        }
    }
}

int main()
{
    std::cin >> N;
    for (int i=1; i<=N; ++i) {
        for (int j=1; j<=N; ++j) {
            std::cin >> a[i][j];
        }
    }
    
    for (int i=1; i<=N; ++i) {
        for (int j=1; j<N; ++j) {
            std::swap(a[i][j], a[i][j+1]);
            getMaxRow(i);
            getMaxCol(j);
            getMaxCol(j+1);
            std::swap(a[i][j], a[i][j+1]);
        }
    }
    for (int j=1; j<=N; ++j) {
        for (int i=1; i<N; ++i) {
            std::swap(a[i][j], a[i+1][j]);
            getMaxRow(i);
            getMaxRow(i+1);
            getMaxCol(j);
            std::swap(a[i][j], a[i+1][j]);
        }
    }
    std::cout << maxCnt;
    return 0;
}