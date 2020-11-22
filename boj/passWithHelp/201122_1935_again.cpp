// 후위 표기식 2
// https://www.acmicpc.net/problem/1935
/*
- 답이 틀렸길래 코너케이스 모르고 백준에서 찾아보니 float이 아닌 double을 쓰면 된다 함
- 실제로 해보니 됨.... 아놔... 앞으로 소수점 계산은 무조건 double로 쓸거다
*/
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

double cal(double a, double b, char op)
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
    
    vector<double> num(num_cnt, 0);
    stack<double> opnd;
    
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
                double a, b;
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