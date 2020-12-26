// 1, 2, 3 더하기 3
// https://www.acmicpc.net/problem/15988
/* 처음엔 쉽다고 생각했는데 계속 안풀려서 결국 풀이를 본 문제
이번에 안 사실은, 반복이 많아지만 recursive는 stack overflow로 답이 안나온다는 것
bottom-up 으로 다시 풀었음
*/
/*
d[n] = d[n-1] + d[n-2] + d[n-3]
1: 1
2: 2
11
2
3: 4
111
12
21
3
4: 7
1111
112
121
211
13
31
22
*/

#include <iostream>

long long s[1000001] = {0, 1, 2, 4, };

// recursive는 반복이 많아지면 stack overflow 나는 것 같음 결과가 안나옴
long long getAnsRecur(int n) {
    if (s[n] == 0) {
        long long ans = getAnsRecur(n-1) + getAnsRecur(n-2) + getAnsRecur(n-3);
        s[n] = ans % 1000000009;
    }
    return s[n];
}

// bottom-up 으로 다시 구해봄
long long getAns(int n) {
    if (s[n] == 0) {
        for (int i=4; i<=n; ++i) {
            s[i] = (s[i-1] + s[i-2] + s[i-3]) % 1000000009;
        }
    }
    return s[n];
}

int main()
{
    int n;
    std::cin >> n;

    while (n--) {
        int input;
        std::cin >> input;
        std::cout << getAns(input) << '\n';
    }
    return 0;
}