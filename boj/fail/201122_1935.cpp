// 후위 표기식 2
// https://www.acmicpc.net/problem/1935
/*
- 후위 표기식 문제 답보고 푼 이후에 바로 푼 거라 나중에 다시 풀수 있도록 해야 함
- cout 이용해서 소숫점 표현하는 거 이번에 찾아보고 알았음
- 분명 예제들은 맞았는데 왜 틀린지 모르겠음. 코너 케이스가 뭘까..?
*/
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

float cal(float a, float b, char op)
{
    switch (op) {
        case '*':
            return a*b;
        case '/':
            return a/b;
        case '+':
            return a+b;
        case '-':
            return a-b; 
    }
    return -1;
}

int main()
{
    int num_cnt;
    cin >> num_cnt;
    
    vector<float> num(num_cnt, 0);
    stack<float> opnd;
    
    string cmd;
    cin >> cmd;
    
    for (int i=0; i<num_cnt; ++i) {
        cin >> num[i];
    }
    
    for (auto& c: cmd) {
        switch (c) {
            case '+':
            case '-':
            case '/':
            case '*':
            {
                float a, b;
                b = opnd.top();
                opnd.pop();
                a = opnd.top();
                opnd.pop();
                opnd.push(cal(a, b, c));
                break;
            }
            default:
            
            {
                opnd.push(num[c - 'A']);
            }
        }
    }
    
    cout << fixed;
    cout.precision(2);
    cout << opnd.top();

    return 0;
}