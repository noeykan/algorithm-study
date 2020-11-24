// 팩토리얼
// https://www.acmicpc.net/problem/10872
/*
- 너무 간단하게 생각해서 구현했다가 시간초과 됨..ㅠㅠ
- 아무리 봐도 틀린것도 아니고 시간초관데, 재귀함수라서 시간이 더걸렸나..?
  이상해서 찾아보니 입력이 0일때를 생각 안했음... 하... 무한루프 돌았던듯...
- 기존 틀렸던 팩토리얼 함수
int factorial(int n) {
    if (n == 1) return 1;
    return n*factorial(n-1);
}
*/

#include <iostream>

using namespace std;

int factorial(int n) {
    if (n <= 1) return 1;
    return n*factorial(n-1);
}

int main()
{
    int n;
    cin >> n;
    
    cout << factorial(n);
    
    return 0;
}
