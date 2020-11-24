// 팩토리얼 0의 개수
// https://www.acmicpc.net/problem/1676
/*
쉽게 봤다가 몇번 계속 틀리고 세번째에 품
1. 팩토리얼 함수 구현했다가 시간 초과
 - 500!은 어마어마한 숫자라 long long 으로도 안됨
2. 단순히 입력숫자를 5로 나눠서 5의 배수 개수 구했는데 틀림
 - 25같은 숫자는 5*5라 5가 두개 있는거 뒤늦게 파악하고 고려해야 함
*/

#include <iostream>

using namespace std;

int getZeroCnt(int n)
{
    return n/5 + n/(5*5) + n/(5*5*5); // 입력이 500까지라 625보다 아래이므로 여기까지만
}

int main()
{
    int input;
    cin >> input;
    
    cout << getZeroCnt(input);
    
    return 0;
}
