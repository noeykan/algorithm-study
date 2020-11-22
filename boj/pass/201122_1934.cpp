// 최소공배수
// https://www.acmicpc.net/problem/1934
/* 2609번 문제에서 이미 최대공약수와 최소공배수 문제 풀어봐서
복습하는 차원에서 다시 한번 품 */
#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main()
{
    int cnt;
    cin >> cnt;
    
    while (cnt--) {
        int a, b, gcd_ans;
        cin >> a >> b;
        
        gcd_ans = a>b ? gcd(a, b) : gcd(b, a);
        cout << a * b / gcd_ans << '\n';
    }
    
    return 0;
}