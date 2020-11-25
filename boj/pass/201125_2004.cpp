// 조합 0의 개수
// https://www.acmicpc.net/problem/2004
/*
- 고생 많이 한 문제
- 처음에 개수를 5로만 계산해서 (2는 당연히 5보다 많으니까) 팩토리얼 문제 풀었었는데
이번에는 컴비네이션이다보니 나눠져서 5만 남고 2는 없는 경우가 있었음 (5C1)
- 결국 2랑 5 개수를 두개 모두 구해야 했고 내 코드에도 문제 있었어서 디버깅하느라 애먹음
- getCnt 파라미터 자료형도 처음엔 int로 충분하다고 생각했는데, 플로팅 런타임 오류 발생
보니까 n/cur_denom 값이 범위를 넘어가는지 에러 났어서 long long으로 바꿈
*/

#include <iostream>
#include <algorithm>

using namespace std;

long long getCnt(long long n, long long denom)
{
    long long cnt = 0;
    long long cur_denom = denom;
    while (n/cur_denom != 0) {
        cnt += n/cur_denom;
        cur_denom *= denom;
    }
    return cnt;
}

int main()
{
    int n, m;
    cin >> n >> m;
    
    long long cntTwo = getCnt(n, 2) - getCnt(n-m, 2) - getCnt(m, 2);
    long long cntFive = getCnt(n, 5) - getCnt(n-m, 5) - getCnt(m, 5);
    
    cout << min(cntTwo, cntFive);
    return 0;
}
