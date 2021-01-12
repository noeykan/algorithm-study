// 타일 채우기
// https://www.acmicpc.net/problem/2133
/* 진짜 몇시간을 생각했는지 모른다 그림그려가면서 ㅠㅠㅠ
결국 점화식을 어떻게 정의하냐가 핵심임... 근데 더 쉬운 풀이가 있네...? */
/*
d[0][n] : n번째에 블럭이 마무리 되는 경우
d[1][n] : n번째에 블럭이 마무리 되지 않는 경우
*/

#include <iostream>

// 나의 풀이
int d[2][15];

int main()
{
    int N;
    std::cin >> N;
    
    if (N % 2 != 0) {
        std::cout << 0;
    } else {
        N = N/2;
        d[0][0] = 3;
        d[1][0] = 2;
        for (int i=1; i<N; ++i) {
            d[0][i] = 3*d[0][i-1] + d[1][i-1];
            d[1][i] = 2*d[0][i-1] + d[1][i-1];
        }
        std::cout << d[0][N-1];
    }
    return 0;
}