// 1,2,3 더하기
// https://www.acmicpc.net/problem/9095

/*
1. 함수의 정의
 f(n) = 정수 n을 1,2,3의 합으로 나타내는 방법의 수
2. 초기값 대입
 f(1) = 1
  1
 f(2) = 2
  1+1
  2
 f(3) = 4
  1+1+1
  1+2
  2+1
  3
 f(4) = 7
  1+1+1+1
  1+1+2
  1+2+1
  2+1+1
  1+3
  3+1
  2+2
 f(4)는 f(3)+1, f(2)+2, f(1)+3 으로 표현 가능
 f(5) = 13
  1+1+1+1+1 
  1+1+1+2
  1+1+2+1
  1+2+1+1
  2+1+1+1
  1+1+3
  1+3+1
  3+1+1
  1+2+2
  2+1+2
  2+2+1
  2+3
  3+2
 f(5)는 f(4)+1, f(3)+2, f(2)+3 으로 표현 가능
 즉, 전의 3항을 더하면 됨!
3. 점화식 만들기
 f(n) = f(n-1)+f(n-2)+f(n-3)
*/

#include <iostream>
using namespace std;

// 계산상 편의를 위해 index는 1부터 시작
int cache[10001]; // 정수의 범위가 안나와있으므로 그냥 만개로 잡음
int tc[11]; // tc는 11보다 작음

int f(const int &n) {
    if (cache[n])
        return cache[n];
    
    if (n == 1) cache[n] = 1;
    else if (n == 2) cache[n] = 2;
    else if (n == 3) cache[n] = 4;
    else {
        cache[n] = f(n-1) + f(n-2) + f(n-3);
    }
    return cache[n];
}

int main()
{
    int tc_cnt;
    int integer;
    cin >> tc_cnt;
    for (int i=1; i<=tc_cnt; ++i)
        cin >> tc[i];       
    for (int i=1; i<= tc_cnt; ++i)
        cout << f(tc[i]) << endl;

    return 0;
}
