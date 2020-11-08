// 덱
// https://www.acmicpc.net/problem/10866

#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main()
{
    int cnt;
    string cmd;
    int arg;
    deque<int> dq;
    
    cin >> cnt;
    
    while (cnt--) {
        cin >> cmd;
        if (cmd == "push_front") {
            cin >> arg;
            dq.push_front(arg);
        } else if (cmd == "push_back") {
            cin >> arg;
            dq.push_back(arg);
        } else if (cmd == "pop_front") {
            if (dq.empty()) {
                cout << -1 << '\n';
            } else {
                cout << dq.front() << '\n';
                dq.pop_front();
            }
        } else if (cmd == "pop_back") {
            if (dq.empty()) {
                cout << -1 << '\n';
            } else {
                cout << dq.back() << '\n';
                dq.pop_back();
            }
        } else if (cmd == "size") {
            cout << dq.size() << '\n';
        } else if (cmd == "empty") {
            if (dq.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        } else if (cmd == "front") {
            if (dq.empty())
                cout << -1 << '\n';
            else
                cout << dq.front() << '\n';
        } else if (cmd == "back") {
            if (dq.empty())
                cout << -1 << '\n';
            else
                cout << dq.back() << '\n';
        } else {
            cout << "Invliad command" << endl;
        }
        
    }
    
    return 0;
}
