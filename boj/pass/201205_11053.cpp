// 가장 긴 증가하는 부분 수열
// https://www.acmicpc.net/problem/11053
/* 거의 2시간 고민하다 푼 문제.. 하고나면 쉬운데 왜이렇게 생각하는게 어려울까  */
/*
d[n][k] = 수열이 n개 일 때 마지막이 k인  가장 긴 증가하는 부분 수열 길이

10 20 10 30 20 50 
   
 n k 10 20 30 40 50
 1    1  0  0  0  0
 2    1  2  0  0  0
 3    1  2  0  0  0
 4    1  2  3  0  0
 5    1  2  3  0  0
 6    1  2  3  0  4

d[n][k] = max(d[n-1][1],...,d[n-1][k-1]) + 1

잉... 잠깐만..? 2중배열 필요가 없네...? 하나씩 업데이트만 해주면 되는구나..? 헐랭
*/

int d[1001];

#include <iostream>

using namespace std;

int main()
{
    int n, a;
    cin >> n;
    
    int ans = 0;
    while (n--) {
        int maxCnt = 0;
        cin >> a;
        for (int i=1; i<a; ++i) {
            if (maxCnt < d[i]) {
                maxCnt = d[i];
            }
        }
        d[a] = maxCnt + 1;
        if (ans < d[a])
            ans = d[a];
    }

    cout << ans;
    
    return 0;
}

/* 백준 코드에서 본 기발한 풀이법 */
/*
#include <stdio.h>
#include <algorithm>
using namespace std;
int main() {
	int n, x, _len = 0, arr[1001] = {};
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		if (arr[_len] < x) arr[++_len] = x;
		else {
			auto it = lower_bound(arr, arr + _len + 1, x);
			*it = x;
		}
	}
	printf("%d", _len);
}
*/