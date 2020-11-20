// ROT13
// https://www.acmicpc.net/problem/11655
/* 쉽게 풀었음 */

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    string line;
    getline(cin, line);
    vector<char> ans;
    
    for (auto& s: line)
    {
        if (s >= 'a' && s <= 'z') {
            ans.push_back(((s - 'a') + 13) % 26 + 'a');
        } else if (s >= 'A' && s <= 'Z') {
            ans.push_back(((s - 'A') + 13) % 26 + 'A');
        } else {
            ans.push_back(s);
        }
    }
    
    for (auto& s: ans)
    {
        cout << s;
    }

    return 0;
}