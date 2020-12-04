// 1, 2, 3 더하기 5
// https://www.acmicpc.net/problem/15990
/* 와 진짜 몇시간동안 고민하다가 결국 못풀어서 블로그 참고함...ㅠ 역대급 난이도
각 어떤 숫자로 끝나는 지 중요해서 관리해야겠다고 생각했는데 어떤 자료구조를 
쓸 지 몰라서 몰랐는데 2차원 배열로 하면 됐구먼... 게다가 점화식 정의를 생각 못했다

문제 풀이가 좀 조잡한데 더 간단한 알고리즘 없을까..? */
/*
1: 1
2: 1
3: 3
 1 2
 2 1
 3
4: 3
 1 2 1
 1 3
 3 1
5: 4
 1 3 1
 2 1 2
 2 3
 3 2
6: 8
 1 2 1 2
 2 1 2 1
 1 2 3 
 1 3 2 
 2 1 3 
 2 3 1 
 3 1 2 
 3 2 1 
*/
/*
2차원 배열 점화식
d[n][k] : k으로 더하기가 끝나는 n
d[n][1] = d[n-1][2] + d[n-1][3]
d[n][2] = d[n-2][1] + d[n-2][3]
d[n][3] = d[n-3][1] + d[n-3][2]

ex)
d[4][1] = d[3][2] + d[3][3] = 1 + 1
d[4][2] = d[2][1] + d[2][3] = 0 + 0
d[4][3] = d[1][1] + d[1][2] = 1 + 0

d[5][1] = d[4][2] + d[4][3] = 0 + 1
d[5][2] = d[3][1] + d[3][3] = 1 + 1
d[5][3] = d[2][1] + d[2][2] = 0 + 1
*/

#include <iostream>
#include <algorithm>

#define MAX_NUM 100000
#define DIVISOR 1000000009
using namespace std;
long long d[MAX_NUM+1][4];

long long getWays(int n, int k) {
    if (d[n][k] == -1) {
        if (k == 1)
            d[n][k] = (getWays(n-1, 2) + getWays(n-1, 3)) % DIVISOR;
        else if (k == 2)
            d[n][k] = (getWays(n-2, 1) + getWays(n-2, 3)) % DIVISOR;
        else
            d[n][k] = (getWays(n-3, 1) + getWays(n-3, 2)) % DIVISOR;
    }
    return d[n][k];  
}

int main()
{
    fill(&d[0][0], &d[MAX_NUM][4], -1);
    d[1][1] = d[2][2] = d[3][3] = d[3][1] = d[3][2] = 1;
    d[1][2] = d[1][3] = d[2][1] = d[2][3] = 0;
    
    int n;
    cin >> n;
    
    while (n--) {
        int input;
        cin >> input;
        cout <<
            ( getWays(input, 1) + getWays(input, 2) + getWays(input, 3) ) % DIVISOR << '\n';
    }
    
    return 0;
}