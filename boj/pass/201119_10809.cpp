// 알파벳 찾기
// https://www.acmicpc.net/problem/10809
/* 쉬어가는 문제. 매우 쉬웠음 */

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> bin(26, -1);

    string words;
    cin >> words;
    
    for (int i=0; i<words.size(); i++) {
        if (bin[words[i]-'a'] == -1) {
            bin[words[i]-'a'] = i;
        }
    }
    
    for (auto& n : bin) {
        cout << n << " ";
    }

    return 0;
}