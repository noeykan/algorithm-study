// 가장 긴 증가하는 부분 수열 4
// https://www.acmicpc.net/problem/14002
/* 바로 전에 가장 긴 증가하는 부분 수열 풀어서 쉽게 풀 줄 알았는데 완전 실패했음
덕분에 고민하다가 블로그 찾아서 풀이 다 읽어보고 겨우 내걸로 만들었음
다시 풀어봐야 할 듯 */
/*
d[n][k] = 수열이 n개 일 때 마지막이 k인 가장 긴 증가하는 부분 수열 길이
d[n][k] = min(d[n-1][1],...,d[n-1][k-1]) + 1

10 20 10 30 20 50

        a[0]   a[1]    a[2]    a[3]    a[4]    a[5]
         10     20     10     30     20     50
i,j    cnt[0] cnt[1] cnt[2] cnt[3] cnt[4] cnt[5]
          1      1       1      1      1      1
1,0      1      2       1      1      1      1
3,0      1      2       1      2      1      1
3,1      1      2       1      3      1      1
4,0      1      2       1      3      2      1
5,0      1      2       1      3      2      2
5,1      1      2       1      3      2      3
5,3      1      2       1      3      2      4
             	   	     	      ret
           		     	      idx
     prv[0] prv[1] prv[2] prv[3] prv[4] prv[5]
                  0 
                                  0
	  	      1
			 0
			          0
			          1
			          3
*/

#include <iostream>
#include <vector>
#include <stack>

#define MAX_NUM 1000

std::vector<int> a(MAX_NUM);
std::vector<int> cnt(MAX_NUM, 1);
std::vector<int> prev(MAX_NUM, -1);

int main()
{
    int n;
    std::cin >> n;
    
    for (int i=0; i<n; ++i) {
        std::cin >> a[i];
    }
    
    int maxIdx = 0;
    int maxCnt = 1;
    for (int i=0; i<n; ++i) {
        for (int j=0; j<i; ++j) {
            if (a[j] < a[i] && cnt[j] >= cnt[i]) {
                cnt[i] = cnt[j] + 1;
                prev[i] = j;
                if (cnt[i] > maxCnt) {
                    maxCnt = cnt[i];
                    maxIdx = i;
                }
            }
        }
    }
    
    std::cout << maxCnt << '\n';

    std::stack<int> seq;
    int idx = maxIdx;
    while (idx != -1) {
        seq.push(a[idx]);
        idx = prev[idx];
    }
    
    while (!seq.empty()) {
        std::cout << seq.top() << " ";
        seq.pop();
    }
    
    return 0;
}