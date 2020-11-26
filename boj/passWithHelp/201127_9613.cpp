// GCD 합
// https://www.acmicpc.net/problem/9613
/*
- 얼마 전에 gcd를 유클리드 호제법으로 코딩 했었어서 쉬웠음...이라고 쓰려 했는데
계속 틀렸다고 나오고 범위도 문제없는 것 같고 했는데....이유 모르겠어서
문제 검색하다보니 하... 입력에서랑 나눌때는 int로 되는데 sum은 int 범위 초과할 수 있겠구나 ㅠㅠ
범위 진짜 잘 봐야되는 구나. long long...
*/

#include <iostream>
#include <vector>

using namespace std;

int getGcd(int a, int b)
{
    if (a < b) {
        int tmp;
        tmp = b;
        b = a;
        a = tmp;
    }
    if (b == 0)
        return a;
    return getGcd(b, a%b);
}

int main()
{
    int caseCnt, numCnt;
    int num;
    long long sum;
    cin >> caseCnt;
    
    while (caseCnt--) {
        vector<int> numVec;
        sum = 0;
        cin >> numCnt;
        while (numCnt--) {
            cin >> num;
            numVec.push_back(num);
        }
        
        for (int i=0; i<numVec.size()-1; ++i) {
            for (int j=i+1; j<numVec.size(); ++j) {
                sum += getGcd(numVec[i], numVec[j]);
            }
        }
        cout << sum << '\n';
    }
    
    return 0;
}
