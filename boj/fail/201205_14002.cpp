// 가장 긴 증가하는 부분 수열 4
// https://www.acmicpc.net/problem/14002
/* 바로 전에 가장 긴 증가하는 부분 수열 풀어서 쉽게 풀 줄 알았는데 실패했음
예제 돌리면 맞는 것 같은데 일반적인 답은 안나오나 봄 */
/*
d[n][k] = 수열이 n개 일 때 마지막이 k인 가장 긴 증가하는 부분 수열 길이
d[n][k] = min(d[n-1][1],...,d[n-1][k-1]) + 1

*/

int d[1001];

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int n, a;
    cin >> n;
    
    
    int ansIdx, ansCnt = 0;
    while (n--) {
        int maxCnt = 0;
        int maxIdx = 0;
        
        cin >> a;
        for (int i=1; i<a; ++i) {
            if (d[i] > maxCnt) {
                maxCnt = d[i];
                maxIdx = i;
            }
        }
        d[a] = maxCnt + 1;
        if (ansCnt < d[a]) {
            ansCnt = d[a];
            ansIdx = a;
        }
    }
    
    cout << ansCnt << endl;
    
    stack<int> st;
    for (int i=ansIdx; i>=1; --i) {
        if (d[i] == ansCnt) {
            st.push(i);
            ansCnt--;
        }
    }
    
    while (!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }
    
    return 0;
}