// Alcoholic
// https://atcoder.jp/contests/abc189/tasks/abc189_b
/* 너무 쉬운 문제인데 콘테스트 중에 풀때 계속 하나가 fail 떠서 고민하다가 결국 못풀었음
알고보니 floating error(precision error) 때문... 앞으로 double 형을 비교하는 걸 하지 말고 int 형으로 바꾸자 */

#include <iostream>

using namespace std;

int main()
{
    int n, x;
    cin >> n >> x;
    
    double alcohol = 0;
    int isDrunken = 0;
    int v, p;
    for (int i=1; i<=n; ++i) {
        cin >> v >> p;
        alcohol += v * p;
        if (alcohol > x * 100) {
            cout << i;
            isDrunken = 1;
            break;
        }
    }
    if (!isDrunken) {
        cout << -1;
    }
    
    return 0;
}
