// 오큰수
// https://www.acmicpc.net/problem/17298
/*
- Brute force로 시간초과에 걸려서 풀지 못하고 결국 답을 보고 다시 구현 해봄 ㅠㅠ
- 배열 초기화 할 때 무심코 arr = {-1, }; 이렇게 했는데 첫번째를 제외한 나머지가 0이 되었음 주의
- 초기화도 그렇고 이렇게 input이 개수가 가변적일 수 있는 문제는 속도가 살짝 느려도 배열 대신 '벡터'를 쓰도록 해보자!
*/
#include <iostream>
#include <stack>
#include <vector>

#define MAX_NUM 1000000

using namespace std;

int main()
{
    int cnt;
    int tmp;
    stack<int> st;
    //int in[MAX_NUM];
    //int ans[MAX_NUM] = {-1, }; // 이렇게 쓰면 초기화 나머지 0됨
    
    cin >> cnt;
    vector<int> ans(cnt, -1);
    vector<int> in(cnt, 0);
    
    for (int i=0; i<cnt; ++i) {
        cin >> in[i];
    }
    
    for (int i=0; i<cnt; ++i) {
        while (!st.empty() && in[st.top()] < in[i] ) {
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
