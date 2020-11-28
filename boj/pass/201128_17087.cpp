// 숨바꼭질 6
// https://www.acmicpc.net/problem/17087
/* 여러 숫자의 최대공약수를 구하는 걸 고민하다가 다음날 푼 문제 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

long long getGcd(long long a, long long b)
{
    if (a < b) {
        swap(a, b);
    }
    if (b == 0)
        return a;
    
    return getGcd(b, a%b);
}

int main()
{
    int n;
    long long s;
    
    cin >> n >> s;
    vector<long long> a(n, 0);
    
    for (auto& e: a) {
        long long in;
        cin >> in;
        e = abs(in - s);
    }
    
    long long ans = a[0];
    for (auto e: a) {
        ans = getGcd(ans, e);
    }
    
    cout << ans;
    return 0;
}
