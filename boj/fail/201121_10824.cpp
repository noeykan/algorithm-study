// 네 수
// https://www.acmicpc.net/problem/10824
/* 코드는 좀 맘에 안드는데 분명 맞는 것 같은데 백준에서 틀렸다고 나옴
뭔가 코너케이스가 있나보다.. 해답을 봐야겠다.. */

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    
    vector<int> ab(15, 0);
    vector<int> cd(15, 0);
    vector<int> ans(15, 0);
    
    cin >> a >> b >> c >> d;
    
    int pos;
    for (pos=0; b != 0; ++pos) {
        ab[pos] = b % 10;
        b /= 10;
    }
    for (; a != 0; ++pos) {
        ab[pos] = a % 10;
        a /= 10;
    }
    
    for (pos=0; d != 0; ++pos) {
        cd[pos] = d % 10;
        d /= 10;
    }
    for (; c != 0; ++pos) {
        cd[pos] = c % 10;
        c /= 10;
    }
    
    for (int i=0; i<ab.size()-1; ++i) {
        ans[i] = ans[i] + ((ab[i] + cd[i]) % 10);
        ans[i+1] = (ab[i] + cd[i]) / 10;
    }
    
    bool isStarted=false;
    for (int i = ans.size() - 1; i >= 0; --i)
    {
        if (ans[i] != 0)
            isStarted = true;
        if (isStarted)
            cout << ans[i];
    }
    if (!isStarted)
        cout << 0;

    return 0;
}