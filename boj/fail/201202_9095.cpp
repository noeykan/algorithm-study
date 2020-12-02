// 1, 2, 3 더하기
// https://www.acmicpc.net/problem/9095
/* 몇년 전에 풀었던 문젠데 다시 규칙 알아내는데 거의 1시간 가까이 걸림 ㅠㅠ
규칙 알아내기가 진짜 쉽지 않다.. 근데 문제는 그 규칙이 내가 문제를 잘못 봐서 -_- 틀린 규칙이었음
1,2,3 이상 모든 조합을 쓰는 줄 알았어서... f(5) 부터 답이 안맞기 시작... 하... */
/*
f(1) = 0

f(2) = 1
 1+1

f(3) = 3
 1+2
 2+1

 f(2)
 (1+1)+1, 

f(4) = 7
 3+1
 2+2
 1+3

 f(3)
 (1+1+1)+1
 (1+2)+1
 (2+1)+1

 f(2)
 (1+1)+2 

f(5)
 1+4
 2+3
 3+2
 4+1

 f(4)
 (1+1+1+1)+1
 (1+1+2)+1
 (1+2+1)+1
 (2+1+1)+1
 (2+2)+1
 (1+3)+1
 (3+1)+1

 f(3)
 (1+1+1)+2
 (1+2)+2
 (2+1)+2

 f(2)
 (1+1)+3 
*/

#include <iostream>

using namespace std;

int cache[11];

int getCnt(int n) {
    if (cache[n] == 0) {
        if (n == 1) cache[n] = 0;
        else if (n == 2) cache[n] = 1;
        else {
            int cnt = n - 1;
            for (int i=n-1; i>=2; --i) {
                cnt += getCnt(i);
            }
            cache[n] = cnt;
        }
    }
    return cache[n];
}

int main()
{
    int nCase, n;
    cin >> nCase;
    
    while (nCase--) {
        cin >> n;
        cout << n << ": " << getCnt(n) << '\n';
    }

    return 0;
}
