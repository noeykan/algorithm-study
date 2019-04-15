// 2xn 타일링
// https://www.acmicpc.net/problem/11726

#include <iostream>
using namespace std;

unsigned int cache[1001]; // 1<=n<=1000, 1??? ??

unsigned int f(unsigned int n) {
    if (cache[n]) {
        return cache[n];
    }
    switch(n) {
        case 1:
            cache[n] = 1;
            break;
        case 2:
            cache[n] = 2;
            break;
        default:
            cache[n] = (f(n-1) + f(n-2)) % 10007;
            break;
    }
    return cache[n];
}

int main()
{
    int n;
    cin >> n;
    cout << f(n);
    return 0;
}
