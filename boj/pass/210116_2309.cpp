// https://www.acmicpc.net/problem/2309
// 일곱 난쟁이
/* 아 진짜 반례찾느라 개고생했는데 ㅠㅠㅠㅠ
if ()
  a;
  b;
이런식으로 {} 로 안묶어서 a; 만 실행돼서 그런거였다....와 진짜
괄호 하나 때문에 이런 고생을 하다니.. 무조건 {}로 묶는 습관 길러야겠다;;
*/
#include <iostream>
#include <algorithm>

#define N 9

int a[N];

int main()
{
    int sum = 0;
    for (int i=0; i<N; ++i) {
        std::cin >> a[i];
        sum += a[i];
    }

    int ex1, ex2;
    std::sort(a, a+N);
    for (int i=0; i<N-1; ++i) {
        for (int j=i+1; j<N; ++j) {
            if (a[i] + a[j] == sum - 100) {
                ex1 = i;
                ex2 = j;
            }
        }
    }
    for (int i=0; i<N; ++i) {
        if (i != ex1 && i != ex2) {
            std::cout << a[i] << '\n';
        }
    }

    return 0;
}
