// 8진수 2진수
// https://www.acmicpc.net/problem/1212
/* 바로 전에 2진수->8진수 풀어봐서 쉽게 풀긴 했음.
다만 reverse를 쓰지 않고 뒷자리 부터 계산하지 않고 앞자리부터 바로 계산하는 걸 하려니,
그리고 맨 앞에는 0을 안붙이려고 하고, 0은 0이 나와야하니 좀 코드가 맘에 안드네
생각보다 많이 틀렸다. 은근 예외 케이스가 많았던 듯*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string oct, bin;
    cin >> oct;
    
    int num, i;
    for (i=0; i<oct.size(); ++i) {
        bin += to_string((oct[i]-'0') / 4);
        bin += to_string(((oct[i]-'0') % 4) / 2);
        bin += to_string((oct[i]-'0') % 2);
    }
    
    for (i=0; i<bin.size(); ++i) {
        if (bin[i] != '0')
            break;
    }
    if (i == bin.size())
        cout << 0;
    else
        cout << bin.substr(i);
    return 0;
}