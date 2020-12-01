// Base Conversion
// https://www.acmicpc.net/problem/11576
/* 쉽게 풀었음 */

#include <iostream>
#include <stack>
#include <cmath>

using namespace std;

int main()
{
    int baseFrom, baseTo;
    int digit;
    
    cin >> baseFrom >> baseTo;
    cin >> digit;
    
    stack<int> numBefore;
    while (digit--) {
        int input;
        cin >> input;
        numBefore.push(input);
    }
    
    int numBase10 = 0;
    digit = 0;
    while (!numBefore.empty()) {
        numBase10 += numBefore.top()*pow(baseFrom, digit++);
        numBefore.pop();
    }
    
    stack<int> numAfter;
    while (numBase10 != 0) {
        numAfter.push(numBase10 % baseTo);
        numBase10 = numBase10 / baseTo;
    }
    
    while (!numAfter.empty()) {
        cout << numAfter.top() << " ";
        numAfter.pop();
    }

    return 0;
}
