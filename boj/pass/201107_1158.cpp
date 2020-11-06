// 요세푸스 문제
// https://www.acmicpc.net/problem/1158
/*
문제 유형이 주어지고 푸는 시기여서 쉽게 풀 수 있었던 것 같다.
원래는 연결 링크드리스트를 구현해서 풀려고도 해봤는데 굳이 그럴 필요 없었음
*/
#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    int n;
    int k;
    int cnt = 1;
    int tmp;
    queue<int> q;
    
    cin >> n >> k;
    
    for (int i=1; i<=n; ++i) {
        q.push(i);
    }
    cout << "<";
    while (!q.empty()) {
        tmp = q.front();
        q.pop();
        if (cnt++ % k == 0) {
            cout << tmp;
            if (!q.empty())
                cout << ", ";
        } else {
            q.push(tmp);
        }
    }
    cout << ">";
    return 0;
}
