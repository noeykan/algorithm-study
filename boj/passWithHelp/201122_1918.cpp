// 후위 표기식
// https://www.acmicpc.net/problem/1918
/*
며칠을 고민했는데도 풀지 못했던 문제... 결국 블로그 답보고 이해한 후 풀었다
알고보면 쉬운 것 같으면서도 알기 전엔 참 어렵다.. 다시 풀어보자!
*/
#include <iostream>
#include <stack>

using namespace std;

int priority(char c)
{
    switch (c) {
        case '*':
        case '/':
            return 2;
        case '+':
        case '-':
            return 1;
        case '(':
        case ')':
            return 0;
    }
    return -1;
}

int main()
{
    stack<char> st;
    string ans;
    string cmd;
    cin >> cmd;
    
    for (auto& c: cmd) {
        switch (c) {
            case '+':
            case '-':
            case '*':
            case '/':
                while (!st.empty() && priority(st.top()) >= priority(c)) {
                    ans += st.top();
                    st.pop();
                }
                st.push(c);
                break;
            case ')':
                while (!st.empty() && st.top() != '(') {
                    ans += st.top();
                    st.pop();
                }
                st.pop();
                break;
            case '(':
                st.push(c);
                break;
            default:
                ans += c;
                break;
        }
    }
    
    while(!st.empty()) {
        ans += st.top();
        st.pop();
    }
    
    cout << ans;
    return 0;
}