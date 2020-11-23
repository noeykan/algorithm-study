// 골드바흐의 추측
// https://www.acmicpc.net/problem/6588
/*
- 이 전에 소수 구하는 문제 풀어서 풀 수 있었던 것 같음
- 한번 시간 초과 떠서 틀렸었는데, 소수 배열 구하는 걸 가장 큰 수 기준으로 한번만 하니까
시간 안에 들어왔음
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    int numMax = 0;
    vector<int> num;
    vector<bool> isPrime(1000001, true);
    isPrime[1] = false;

    while (1) {
        cin >> n;
        num.push_back(n);
        if (n > numMax)
            numMax = n;
        if (n == 0) break;
    }
    
    for (int i=2; i*i<=numMax; ++i) {
        if (isPrime[i] == false)
            continue;
        for (int j=i*2; j<=numMax; j+=i) {
            isPrime[j] = false;
        }
    }
    
    for (auto n: num) {
        for (int i=n; i>=2; --i) {
            if (isPrime[i] && isPrime[n-i]) {
                cout << n << " = " << n-i << " + " << i << '\n';
                break;
            }
            if (i == 2)
                cout << "Goldbach's conjecture is wrong." << '\n';
        }
    }
    
    return 0;
}
