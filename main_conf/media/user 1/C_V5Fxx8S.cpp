#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, m, a[42];
int vis[42] , ok;

void fun( int cur, int step )
{
    if( cur == n && step == m ){
        ok = 1;
        return;
    }
    if( vis[cur] != -1 ) return;

    int x = a[cur];
    set<int>st;

    for(int i=2; i*i <= x; i++){
        if( n%i == 0 ){
            st.insert(i);
            while( x%i == 0 ) x /= i;
        }
    }
    if( x > 1 ) st.insert(x);

    for(auto i:st ){
        if( cur-i >= 1 ){
            vis[cur-i] = 1;
            fun( cur-i , step+1 );
        }

        if( cur+i <= n ){
            vis[cur+i] = 1 ;
            fun( cur+i , step+1 );
        }
    }
}


int main()
{
    ios::sync_with_stdio(0);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
 	freopen("output.txt", "w", stdout);
#endif

    int t; cin>>t;

    while(t--){
        memset(vis,-1,sizeof vis);
        cin>>n;
        for(int i=1; i<=n; i++) cin>>a[i];
        ok = 0; cin>>m; fun(1,0);
        if( ok  ) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

    return 0;
}
