// 네 수
// https://www.acmicpc.net/problem/10824
/* 배열로 만들어서 한자리씩 더하는 걸로 한번 풀었는데 맞는 것 같은데 실패했다고 떠서
다시 도전. long long 을 써서 비교적 쉽게 풀었다. 그 전까지 long long 쓸 생각 못했음
전에 풀이는 왜 틀렸을까...후...*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    unsigned long long ab;
    unsigned long long cd;
    
    unsigned long long a;
    unsigned long long b;
    unsigned long long c;
    unsigned long long d;
    
    cin >> a >> b >> c >> d;
    
    unsigned long long tmp = b;
    int digit = 1;
    while (tmp / 10 != 0) {
        digit++;
        tmp = tmp/10;
    }
    
    ab = a * pow(10, digit) + b;
    
    tmp = d;
    digit = 1;
    while (tmp / 10 != 0) {
        digit++;
        tmp = tmp/10;
    }
    
    cd = c * pow(10, digit) + d;
    
    cout << ab + cd;
    return 0;
}