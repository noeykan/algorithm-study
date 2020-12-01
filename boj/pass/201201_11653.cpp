// 소인수분해
// https://www.acmicpc.net/problem/11653
/* 계속 틀려서 질문 검색해서 봤는데 문제가 좀 이상한듯
결론적으로 1을 넣으면 1이 나와야 하는건데, 그게 아니라 1을 넣으면 아무것도 출력 안해야 답임*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int input;
    cin >> input;

    int num = input;
    for (int i=2; i<=input; ++i) {
        while (num % i == 0) {
            cout << i << '\n';
            num = num / i;
        }
        if (num == 1)
            break;
    }

    return 0;
}
