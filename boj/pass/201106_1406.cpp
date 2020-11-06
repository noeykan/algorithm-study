// 에디터
// https://www.acmicpc.net/problem/1406
/*
- for (auto& c: string) 에서 c가 char인데 string으로 처음에 착각함
- char 문자는 서로 == 가 가능한데 string으로 무조건 처리하려다 보니 시간 소비함
- 전에도 그런 것 같은데 이번에도 똑같이 무한루프에 빠져버림
- 커서 옮길때는 잘 생각하다가도 마지막에 오른쪽 stack에 다 옮길때 꼭 왼쪽 stack pop을 까먹는다
*/
#include <stdio.h>
#include <iostream>
#include <stack>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    int cnt;
    string line;
    char cmd;
    char arg;
    stack<char> left;
    stack<char> right;
    
    cin >> line;
    cin >> cnt;

    for (auto& c: line) {
        left.push(c);
    }
    while (cnt--) {
        cin >> cmd;
        if (cmd == 'L') {
            if (!left.empty()) {
                right.push(left.top());
                left.pop();
            }
        } else if (cmd == 'D') {
            if (!right.empty()) {
                left.push(right.top());
                right.pop();
            }
        } else if (cmd == 'B') {
            if (!left.empty()) {
                left.pop();
            }
        } else if (cmd == 'P') {
            cin >> arg;
            left.push(arg);
        } else {
            cout << "Wrong command!" << endl;
        }
    }
    
    while (!left.empty()) {
        right.push(left.top());
        left.pop();
    }
    
    while (!right.empty()) {
        cout << right.top();
        right.pop();
    }
    
    return 0;
}