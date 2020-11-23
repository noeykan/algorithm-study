// 소수 구하기
// https://www.acmicpc.net/problem/1929
/*
이 전에 소수 구하는 문제 풀어서 풀 수 있었던 것 같음
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    vector<bool> isPrime(b+1, true);
    isPrime[1] = false;
    for (int i=2; i*i<=b; ++i) {
        if (isPrime[i] == false)
            continue;
        for (int j=i*2; j<=b; j+=i) {
            isPrime[j] = false;
        }
    }
    
    for (int i=a; i<=b; ++i) {
        if (isPrime[i])
            cout << i << '\n';
    }
    return 0;
}
