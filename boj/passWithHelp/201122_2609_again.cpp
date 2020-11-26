// 최대공약수와 최소공배수
// https://www.acmicpc.net/problem/2609
/* 이미 푼 문젠데, 혹시나 해서 찾아보니 훨씬 쉬운 방법이 있어서 다시 보고 풂
이번에 유클리드 호제법을 찾아보고 알아보는 기회가 되었음*/
#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main()
{
    int a, b, gcd_ans;
    cin >> a >> b;
    
    gcd_ans = a>b ? gcd(a, b) : gcd(b, a);
    
    cout << gcd_ans << endl;
    cout << a * b / gcd_ans;
    
    return 0;
}