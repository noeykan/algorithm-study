// 스택
// https://www.acmicpc.net/problem/10828

#include <stdio.h>
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int cnt;
    int num;
    string cmd;
    stack<int> st;
    
    cin >> cnt;
    while (cnt--) {
        cin >> cmd;
        if (cmd == "push") {
            cin >> num;
            st.push(num);
        } else if (cmd == "top") {
            if (st.size() == 0)
                cout << -1 << endl;
            else
                cout << st.top() << endl;
        } else if (cmd == "size") {
            cout << st.size() << endl;
        } else if (cmd == "empty") {
            cout << st.empty() << endl;
        } else if (cmd == "pop") {
            if (st.size() == 0) {
                cout << -1 << endl;
            } else {
                cout << st.top() << endl;
                st.pop();
            }
        } else {
        }
    }
    return 0;
}
