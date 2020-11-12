// 오큰수
// https://www.acmicpc.net/problem/17298
/*
brute force 방식으로 풀었는데 '시간초과'로 fail났음. 좀 더 생각해보고 안되면 답 봐야될듯
*/
#include <iostream>
#define MAX_NUM 1000000
using namespace std;

int main()
{
    int arr[MAX_NUM] = {0,};
    int cnt;
    cin >> cnt;
    
    for (int i=0; i<cnt; ++i) {
        cin >> arr[i];
    }
    
    for (int i=0; i<cnt; ++i) {
        for (int j=i; j<cnt; ++j) {
            if (arr[i] < arr[j]) {
                cout << arr[j] << " ";
                break;
            }
            if (j == cnt-1) {
                cout << -1 << " ";
            }
        }
    }
    return 0;
}