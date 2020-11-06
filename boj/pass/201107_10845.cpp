// 큐
// https://www.acmicpc.net/problem/10845

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    int cnt;
    int input;
    string cmd;
    queue<int> q;
    
    cin >> cnt;
    
    while (cnt--) {
        cin >> cmd;
        if (cmd == "push") {
            cin >> input;
            q.push(input);
        } else if (cmd == "pop") {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                cout << q.front() << '\n';
                q.pop();
            }
        } else if (cmd == "size") {
            cout << q.size() << '\n';
        } else if (cmd == "empty") {
            if (q.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        } else if (cmd == "front") {
            if (q.empty())
                cout << -1 << '\n';
            else
                cout << q.front() << '\n';
        } else if (cmd == "back") {
            if (q.empty())
                cout << -1 << '\n';
            else
                cout << q.back() << '\n';
        } else {
            cout << "Invalid command!\n";
        }
    }
    return 0;
}
