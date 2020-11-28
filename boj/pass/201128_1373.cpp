// 2진수 8진수
// https://www.acmicpc.net/problem/1373
/* 내가 고민해서 푼 문제인데 reverse를 두번하는게 좀 걸렸었음
주석 처리 해 놓은 코드는 백준 해답인데 확장성은 좀 떨어져도 속도가 빠르고 깔-끔
특히 예외 처리가 예술 */

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

// 나의 풀이

int main()
{
    string bin;
    string oct;
    int oneOct = 0;
    cin >> bin;

    reverse(bin.begin(), bin.end());
    
    for (int i=0; i<bin.size(); ++i) {
        oneOct += (bin[i]-'0') * pow(2, i%3);
        if (i%3==2 || i == bin.size()-1) {
            oct.append(to_string(oneOct));
            oneOct = 0;
        }
    }
    reverse(oct.begin(), oct.end());

    cout << oct;
    
    return 0;
}

// 백준 풀이
/*
int main()
{
    string s;
    cin >> s;
    
    int size = s.size();
    
    if (size % 3 == 1) {
        cout << s[0];
    }
    else if (size % 3 == 2) {
        cout << (s[0]-'0')*2 + (s[1]-'0');
    }
    
    for (int i=size%3; i<size; i+=3) {
        cout << (s[i]-'0')*4 + (s[i+1]-'0')*2 + (s[i+2]-'0');
    }
    return 0;
}
*/