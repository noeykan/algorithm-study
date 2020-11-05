// 단어뒤집기
// https://www.acmicpc.net/problem/9093
/*
- getline 때문에 고생했던 문제. getline 전에 cin.ignore()를 꼭 해줘야 한다.
- getline 쓸때 맨 끝은 개행문자나 널문자가 없다는 걸 명심
- for (auto& a: line) 으로 했을때 계속 애먹었는데 왜 그랬는지 모르겠다
*/
#include <stdio.h>
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int num;
    string line;
    stack<char> st;
    
    cin >> num;
    cin.ignore();

    while (num--) {
        getline(cin, line);
        line += ' ';
        for (int i=0; i<line.size(); ++i) {
            if (line[i] != ' ') {
                st.push(line[i]);
            }
            else {
                while (!st.empty()) {
                    cout << st.top();
                    st.pop();
                }
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
