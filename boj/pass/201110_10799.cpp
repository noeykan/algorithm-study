// 쇠막대기
// https://www.acmicpc.net/problem/10799
/*
풀긴 했는데, 뭔가 필요 없는 변수를 더 쓴 느낌.
다른 사람 코드를 찾아보니 내가 필요없는 변수 하나 더 써서 빼고 다시 풀어봄
*/

#include <iostream>
#include <string>

using namespace std;

// 내가 처음에 푼 코드
/*
int main()
{
    string cmd;
    int curStickNum = 0;
    int sum = 0;
    bool isShotBefore = false;
    bool isShotReady = false;
    
    cin >> cmd;
    
    for (auto& c: cmd) {
        if (c == '(') {
            ++curStickNum;
            isShotBefore = false;
            isShotReady = true;
        } else if (c == ')') {
            --curStickNum;
            if (!isShotBefore && isShotReady) {
                sum += curStickNum;
                isShotBefore = true;
                isShotReady = false;
            } else {
                ++sum;
                isShotBefore = false;
            }
        } else {
            cout << "Invalid command!";
        }
    }
    cout << sum;
    
    return 0;
}
*/

// 다른 사람 코드 참고 해서 다시 짜본 코드
// 굳이 while 로 안써도 될듯. 난 그냥 string을 for문 돌리는게 더 편한듯
int main()
{
    int curStickNum = 0;
    int sum = 0;
    char c;
    bool isShotReady = false;
    while( (c = getchar()) != '\n' && c != EOF) {
        if (c == '(') {
            ++curStickNum;
            isShotReady = true;
        } else {
            --curStickNum;
            if (isShotReady) {
                sum += curStickNum;
                isShotReady = false;
            } else {
                ++sum;
            }
        }
    }
    cout << sum;
    
    return 0;
}