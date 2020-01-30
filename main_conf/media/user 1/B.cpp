#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(0);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
 	freopen("output.txt", "w", stdout);
#endif


    for(int i=0; i<=20; i++){
        int val = 1 ^ i;
        cout<<i<<' '<<val<<endl;
    }


    return 0;
}
