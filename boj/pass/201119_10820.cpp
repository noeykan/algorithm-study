// 문자열 분석
// https://www.acmicpc.net/problem/10820
/* 쉬어가는 문제. 매우 쉬웠음 */

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    string line;
    while ( getline(cin, line) )
    {
        vector<int> cnt(4, 0);
        for (auto& c : line)
        {
            if (c >= 'a' && c <= 'z')
                cnt[0] += 1;
            else if (c >= 'A' && c <= 'Z')
                cnt[1] += 1;
            else if (c >= '0' && c <= '9')
                cnt[2] += 1;
            else if (c == ' ')
                cnt[3] += 1;
        }
        for (auto& n : cnt)
        {
            cout << n << " ";
        }
        cout << '\n';
    }
    return 0;
}