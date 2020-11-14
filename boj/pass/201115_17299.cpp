// 오등큰수
// https://www.acmicpc.net/problem/17299
/*
- 바로 이 전 문제에서 오큰수를 해답보고 풀었는지라 쉽게 풀었음
- 유일하게 헤맸던 부분이 런타임 에러가 나서였는데, freq 벡터의 크기를
  test case(cnt) 개수로 처음에 잡아서 그랬던 거였음.
*/
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    int cnt;
    int tmp;
    cin >> cnt;

    vector<int> in(cnt, 0);
    vector<int> ans(cnt, -1);
    vector<int> freq(1000000, 0);
    stack<int> st;

    for (int i=0; i<cnt; ++i) {
        cin >> in[i];
        freq[in[i]]++;
    }
    
    for (int i=0; i<cnt; ++i) {
        while (!st.empty() && freq[in[st.top()]] < freq[in[i]]) {
            ans[st.top()] = in[i];
            st.pop();
        }
        st.push(i);
    }
    
    for (int i=0; i<cnt; ++i) {
        cout << ans[i] << " ";
    }
    
    return 0;
}
