// 포도주 시식
// https://www.acmicpc.net/source/12502769

/*
술잔: 6 10 13 9 8 1
최대: 6 16 ?

3번째 술잔의 경우 3가지 경우가 있음
   6 10 13
(1) o o x : f(2)
(2) o x o : f(1) + d(3)
(3) x o o : f(0) + d(2) + d(3)


DP민의 DP 문제 해결 3단계
1) 함수의 정의
 f(n) = 잔이 n개일 때 마신 최대 포도주의 양
2) 초기값 대입
 f(1) = d(1)
 f(2) = d(1) + d(2)
 f(3) = max(f(2), f(1)+d(3), f(0)+d(2)+d(3))
3) 점화식 만들기
 f(n) = max(f(n-1), f(n-2)+d(n), f(n-3)+d(n-1)+d(n));
*/

#include <iostream>
#include <algorithm> // max
using namespace std;

int cache[10001]; // f(n)에 대한 cache 저장
int d[10001]; // 포도주 잔의 양

int f(const int &n)
{
    if (cache[n] != -1)
        return cache[n];

    if (n==0) cache[0] = 0;
    else if (n==1) cache[1] = d[1];
    else if (n==2) cache[2] = d[1]+d[2];
    else {
        cache[n] = max<int>(max<int>(f(n-1), f(n-2)+d[n]),
                        f(n-3)+d[n-1]+d[n]);
    }
    return cache[n];
}

int main()
{
    int d_cnt;
    cin >> d_cnt;
    for (int i=1; i<=d_cnt; ++i)
        cin >> d[i];
    fill_n(cache, d_cnt+1, -1); // cache를 -1로 초기화
    cout << f(d_cnt);
    return 0;
}
