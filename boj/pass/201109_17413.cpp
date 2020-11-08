// 단어 뒤집기 2
// https://www.acmicpc.net/problem/17413
/*
풀긴 했지만 코드를 더 효율적으로 최적화할 수 있을까..?
*/
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int cnt;
    bool braketStarted = false;
    string line;
    stack<char> st;
    
    getline(cin, line);
    line += ' ';
    for (auto& c: line) {
        if (c == '<') {
            while (!st.empty()) {
                cout << st.top();
                st.pop();
            }
            braketStarted = true;
            cout << c;
        } else if (c == '>') {
            braketStarted = false;
            cout << c;
        } else if (c == ' ') {
            if (braketStarted) {
                cout << c;
            } else {
                while (!st.empty()) {
                    cout << st.top();
                    st.pop();
                }
                cout << c;
            }
        } else {
            if (braketStarted) {
                cout << c;
            } else {
                st.push(c);
            }
        }
    }
    return 0;
}
