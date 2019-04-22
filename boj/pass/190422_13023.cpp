// ABCDE
// https://www.acmicpc.net/problem/13023

#include <iostream>
#include <vector>

#define MAX_PERSON 2000
#define TARGET_CONNECTED 5
using namespace std;

int cnt_person;
int cnt_relation;
bool found_abcde;

vector<int> graph[MAX_PERSON];
bool isVisited[MAX_PERSON];

void find_abcde(int person, int cnt_connected) {
    if (cnt_connected == TARGET_CONNECTED) {
        found_abcde = true;
        return;
    }
    isVisited[person] = true;
    for (auto p : graph[person]) {
        if (!isVisited[p]) {
            find_abcde(p, cnt_connected+1);
        }
    }
    isVisited[person] = false;
}

int main()
{
    cin >> cnt_person >> cnt_relation;

    while (cnt_relation--) {
        int person1, person2;
        cin >> person1 >> person2;
        graph[person1].push_back(person2);
        graph[person2].push_back(person1);
    }
    
    for (int i=0; i<cnt_person; ++i) {
        find_abcde(i, 1);
        if (found_abcde) break;
    }
    
    cout << found_abcde << endl;
    return 0;
}
