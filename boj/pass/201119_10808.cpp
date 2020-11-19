// 알파벳 개수
// https://www.acmicpc.net/problem/10808
/* 쉬어가는 문제. 매우 쉬웠음 */

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> cnt(26, 0);

    string words;
    cin >> words;
    
    for (auto& c : words) {
        cnt[c - 'a'] += 1;
    }
    
    for (auto& n : cnt) {
        cout << n << " ";
    }

    return 0;
}