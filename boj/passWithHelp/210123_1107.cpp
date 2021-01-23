// 리모컨
// https://www.acmicpc.net/problem/1107
/* 브루트포스 문제 어렵다;; 일단 이게 브루트포스로 풀어야 된다고 생각하는 것도 어려울 것 같고
나는 심지어 브루트 포스로 알고 있었는데도 결국 못풀어서 블로그로 다른 풀이 보고 풀었네
생각보다 쌩으로 다 세는 게 연산량이 많지가 않네 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>

#define MAX_CH 1000000
using namespace std;

int n, m;
vector<int> broken;

int getDigit(int num) {
    if (num == 0)
        return 1;

    int d = 0;
    while (num) {
        num /= 10;
        ++d;
    }
    return d;
}

bool isOkay(int num) {
    if (num == 0) {
        if (find(broken.begin(), broken.end(), 0) == broken.end()) {
            return true;
        } else {
            return false;
        }
    } else {
        while (num) {
            if (find(broken.begin(), broken.end(), num%10) == broken.end()) {
                num /= 10;
            } else {
                return false;
            }
        }
        return true;
    }
}

int getMinCnt(int num) {
    int minCnt = INT_MAX;
    for (int i=0; i<=MAX_CH; ++i) {
        if (isOkay(i)) {
            minCnt = std::min(getDigit(i) + abs(i-n), minCnt);
        }
    }
    return minCnt;
}

int main()
{
    cin >> n >> m;
    for (int i=0; i<m; ++i) {
        int button;
        cin >> button;
        broken.push_back(button);
    }
    
    cout << min(abs(n-100), getMinCnt(n));
    
    return 0;
}
