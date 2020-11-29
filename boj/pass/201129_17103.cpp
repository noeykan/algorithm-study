// 골드바흐 파티션
// https://www.acmicpc.net/problem/17103
/* 며칠전에 골드바흐 문제를 푼적이 있어서 풀 수 있었음
구할 때 조건을 <=n/2를 했어야 했는데 <n/2를 해서 틀렸었음. 6 = 3+3 도 있었음.
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    vector<int> in;
    int maxNum = 0;
    int cnt;
    cin >> cnt;
    
    while (cnt--) {
        int inNum;
        cin >> inNum;
        in.push_back(inNum);
        if (inNum > maxNum)
            maxNum = inNum;
    }

    vector<bool> isPrime(maxNum+1, true);
    for (int i=2; i*i<=maxNum; ++i) {
        if (isPrime[i] == false)
            continue;
        for (int j=2*i; j<=maxNum; j+=i) {
            isPrime[j] = false;
        }
    }

    for (auto n: in) {
        int ans = 0;
        for (int i=2; i<=n/2; ++i) {
            if (isPrime[i] && isPrime[n-i]) {
                ans++;
            }
        }
        cout << ans << '\n';
    }
    
    return 0;
}
