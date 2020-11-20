// 접미사 배열
// https://www.acmicpc.net/problem/11656
/*
처음엔 막막했으나, std::sort를 찾는 과정에서 블로그에 vector도 정렬이 가능한 것을 보고 바로 품
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    string input;
    cin >> input;
    
    vector<string> vec;
    for (int i=0; i<input.size(); ++i) {
        vec.emplace_back(input.substr(i));
    }
    
    sort(vec.begin(), vec.end());
    for (auto& v: vec) {
        cout << v << '\n';
    }
    
    return 0;
}