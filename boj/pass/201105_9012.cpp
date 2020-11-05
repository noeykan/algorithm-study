// 괄호
// https://www.acmicpc.net/problem/9012
/*
- 처음에 stack을 while 바깥에 선언해버려서 왜 안되는지 모르고 꽤 오래 헤맸던 문제
- 결과를 중간에 체크해야 돼서 res 변수를 선언하고 사용하였는데 이를 함수로 만들면 return false; 식으로 조기 리턴을 할 수 있어서 더 편할듯 
- getline 대신 cin으로 받아도 될 뻔 했다
*/
#include <stdio.h>
#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int cnt;
    bool res;
    string line;
    
    cin >> cnt;
    cin.ignore();
    
    while (cnt--) {
        stack<bool> st;
        res = true;
        getline(std::cin, line);
        for (auto& c : line) {
            if (c == '(') {
                st.push(1);
            } else {
                if (st.empty()) {
                    res = false;
                    break;
                } else {
                    st.pop();
                }
            }
        }
        if (res && st.empty()) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}