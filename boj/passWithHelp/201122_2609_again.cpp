// 최대공약수와 최소공배수
// https://www.acmicpc.net/problem/2609
/* 생각보다 생각하는 시간이 좀 걸림 */
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a, b, ans;
    cin >> a >> b;
    
    vector<int> vec;

    for (int i=1; i<=a; ++i) {
        if (a % i == 0) {
            vec.push_back(i);
        }
    }
    
    for (int i=vec.size()-1; i>=0; --i) {
        if (b % vec[i] == 0) {
            ans = vec[i];
            break;
        }
    }
    
    cout << ans << endl;
    cout << ans * (a/ans) * (b/ans);

    return 0;
}