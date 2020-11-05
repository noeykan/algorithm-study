// 스택 수열
// https://www.acmicpc.net/problem/1874
/*
- 은근히 시간 오래 잡아먹고 안풀렸던 문제
- 결국 풀었는데 계속 시간초과 떠서 이해 안되서 고민하다가 백준 게시판가서 힌트 보고 알아낸 문제
- 원인은 바로 'endl'이었다. endl이 있으니 시간초과가 떴음. 다음에 무조건 안써야지.
- stack에 0을 처음에 집어넣는걸 생각해서 조건이 심플해졌다 (stack이 empty인 상황이 없으므로)
- NO 조건일 때 생각해내는 것이 어려웠는데 알고보니 심플. stack의 top의 값이 input값 보다 크면 이미 끝난거. 뒤늦게 깨달았다.
*/

#include <stdio.h>
#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int cnt;
    int in;
    int pushNum = 1;
    string cmd;
    stack<int> st;
    st.push(0);
    
    cin >> cnt;
    while (cnt--) {
        cin >> in;
        while (1) {
            if (st.top() == in) {
                st.pop();
                cmd += '-';
                break;
            }
            else if (st.top() < in) {
                st.push(pushNum++);
                cmd += '+';
            }
            else {
                cout << "NO";
                goto END;
            }
        }
    }
    for (auto& s: cmd) {
        cout << s << '\n';
    }
END:
    return 0;
}
