// 소수 찾기
// https://www.acmicpc.net/problem/1978
/*
- 1부터 일일이 나눠가며 소수 찾는 법 밖에 생각 안나서 블로그 보고 풀었음
최적화를 한 것이, n까지 안가고 루트 n 까지만 검사해도 된다고 수학적으로 증명되었다고 함
예를들어 80이면 8 까지만 조사 하고 난 이후에는 어차피 조사 한 값이니까 (8*10)
- 여기서 더 최적화 화려면 이미 검사한 배열 그대로 사용하거나 아니면 가장 큰 값을 먼저
구하고 한번 배열 완성 시킨 후에 그 배열로 모든 숫자 체크하면 된다.
*/

#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int n)
{
    vector<bool> isPrimeVec(n+1, true);
    isPrimeVec[1] = false;
    for (int i=2; i*i<=n; ++i) {
        if (isPrimeVec[i] == false) {
            continue;
        }
        for (int j=i*2; j<=n; j+=i) {
            isPrimeVec[j] = false;
        }
    }
    return isPrimeVec[n];
}

int main()
{
    int cnt;
    cin >> cnt;
    
    int primeCnt = 0;
    
    while (cnt--) {
        int input;
        cin >> input;
        
        if (isPrime(input))
            primeCnt++;
    }
    cout << primeCnt;
    return 0;
}
