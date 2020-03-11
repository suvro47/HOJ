#include<bits/stdc++.h>
using namespace std;
 
#define sz 1000006
#define EPS 1e-9
#define PI acos(-1.0)
#define INF 10000007
#define LLINF 100000000000000007
 
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define all(x) x.begin(),x.end()
#define FastIO ios::sync_with_stdio(0);
 
typedef long long ll;
typedef pair<int,int> pii;
 
/* bit Operation */
int SetBit(int val,int pos) {return val | (1<<pos) ;}
int ReSet(int val,int pos ) {return val & ~(1<<pos);}
int CheckBit(int val,int pos) {return val & (1<<pos);}
int ReverseBit(int val,int pos) {return val ^ (1<<pos);}
 
/* graph direction */
int dx[] = {-1, -1, -1,  0, 0,  1, 1, 1};
int dy[] = {-1,  0,  1, -1, 1, -1, 0, 1};
 
ll pow(ll x,ll p){ ll ans = 1; while(p--) ans *= x; }
 
vector<pair<int,int>>v;
bool comp(pair<int,int>a,pair<int,int>b)
{
    if(a.second<=b.second) return a.first<=b.first;
    else return 0;
 
}
 
int main()
{
 
    FastIO
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
 	freopen("output.txt", "w", stdout);
#endif
 
    for(int i=0; i<10000000000; i++)
          cout<<11<<endl<<17<<endl;
 
 
 
 
 
 
    return 0;
 
 
}
 
 
 
/*
  input:
  10 4
  2 3 3 1 1 2 1 2 3 3
*/
