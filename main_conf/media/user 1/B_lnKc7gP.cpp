/**
    OJ :
    Program Code :
    Md. Mujahedul Azad (Turin)
    Hajee Mohammad Danesh Science & Technology University
**/

#include<bits/stdc++.h>
using namespace std;

#define pi              2*acos(0.0)
#define all(v)          v.begin(),v.end()
#define ff              first
#define se              second
#define pb              push_back
#define mp              make_pair
#define Sort(a)         sort(all(a))
#define RSort(a)        Sort(a), reverse(all(a))
#define sz(x)           (int)x.size()
#define max3(a,b,c)     max(a, max(b, c))
#define min3(a,b,c)     min(a, min(b, c))
#define maxall(v)       *max_element(all(v))
#define minall(v)       *min_element(all(v))
#define sq(a)           ((a) * (a))
#define abs(x)          (((x)<0)?-(x):(x))
#define precision(x)    cout << setprecision(x) << fixed
#define mem(a,v)        memset(a, v, sizeof(a))
#define fillAra(a,n,v)  fill(a, a+n, v)
#define fillVec(a, v)   fill(all(a), v)
#define countOne(a)     __builtin_popcount(a)
#define parity(a)       __builtin_parity(a)
#define btz(a)          __builtin_ctz(a)
#define gf              << ' ' <<
#define nl              << '\n'
#define cinIg           cin.sync(); cin.get()
#define FasterIO        ios_base::sync_with_stdio(false);cin.tie(NULL)
#define TestCases       int cases, tc; sfi(tc); for(cases=1; cases<=tc; cases++)
#define TestCasespp     int cases, tc; cin>>tc; for(cases=1; cases<=tc; cases++)
#define un(a)           Sort(a), (a).erase(unique(all(a)),a.end())
#define common(a,b)     Sort(a), Sort(b), a.erase(set_intersection(all(a), all(b), a.begin()), a.end())
#define uncommon(a,b)   Sort(a), Sort(b), a.erase(set_symmetric_difference(all(a), all(b), a.begin()), a.end())

/**------- ShortCuts----------*/
typedef long long             ll;
typedef unsigned long long    ull;
typedef double                db;
typedef long double           ldb;
typedef pair<int, int>        pii;
typedef pair<ll, ll>          pll;
typedef pair<int, pii>        iii;
typedef vector<int>           vi;
typedef vector<ll>            vl;
typedef vector<pii>           vii;
typedef vector<iii>           viii;
typedef vector<vi>            vvi;
typedef map<int, int>         mapii;
typedef map<int, bool>        mapib;
typedef map<int, string>      mapis;
typedef set<int>              seti;

/**------- Char Chk----------*/
inline bool isLow(char ch){if(ch>='a' && ch<='z') return true; return false;}
inline bool isUpp(char ch){if(ch>='A' && ch<='Z') return true; return false;}
inline bool isDig(char ch){if(ch>='0' && ch<='9') return true; return false;}

/**------- Double Chk----------*/
inline bool are_equal(db a, db b){return fabs(a-b)<numeric_limits<db>::epsilon();}
inline bool greater_than(db a, db b){return (a-b) > ((fabs(a)<fabs(b)?fabs(b):fabs(a)) * numeric_limits<db>::epsilon());}
inline bool less_than(db a, db b){return (b-a) > ((fabs(a)<fabs(b)?fabs(b):fabs(a)) * numeric_limits<db>::epsilon());}

/**------- Functions ---------*/
template<typename T> string toString(T x){stringstream ss; ss<<x; return ss.str();}
template<typename T> T SOD(T n){__typeof(n) sum=0, i=1; for(; i*i<=n; i++) sum += (n%i)?0:((sq(i)==n)?i:i+n/i); return sum;}
template<typename T> T stringToT(string s, T a){T p; istringstream ss(s); ss>>p; return p;}

template<typename T>ostream& operator << (ostream& os, const vector<T> &v){os << "["; for(int i=0; i<v.size(); i++){ os << v[i]; if(i != sz(v)-1) os << ", ";} os << "]"; return os;}
template<typename T>ostream& operator << (ostream& os, const set<T> &v){ os << "["; for(auto it : v){os << it;if(it != *v.rbegin())os << ", ";}os << "]";return os;}
template<typename T, typename S> ostream& operator << (ostream& os, const map<T, S> &v){for(auto it : v) os << it.ff << " : " << it.se nl; return os;}
template<typename T, typename S> ostream& operator << (ostream& os, const pair<T, S> &v){os << "(" << v.ff << ", " << v.se << ")";return os;}

ll power(ll a, ll b){ll res = 1; while(b){if(b & 1) res *= a; a = sq(a); b >>= 1;} return res;}
ll bigmod(ll a, ll b, ll m) {ll res = 1; while(b) { if(b & 1) { res = ( (res % m) * (a % m) ) %m ; } a= ((a%m) * (a%m)) %m; b >>= 1; } return res; }
ll modInverse(ll a, ll m) {return bigmod(a,m-2,m);}

/**------- Scanf----------*/
#define sf                 scanf
#define sfi(a)             scanf("%d", &a)
#define sfc(a)             scanf("%c", &a)
#define sfl(a)             scanf("%lld", &a)
#define sfu(a)             scanf("%llu", &a)
#define sfs(a)             scanf("%s", a)
#define sfd(a)             scanf("%lf", &a)
#define sfii(a, b)         scanf("%d %d", &a, &b)
#define sfll(a, b)         scanf("%lld %lld", &a, &b)
#define sfuu(a, b)         scanf("%llu %llu", &a, &b)
#define sfdd(a, b)         scanf("%lf %lf", &a, &b)
#define sfiii(a, b, c)     scanf("%d %d %d", &a, &b, &c)
#define sflll(a, b, c)     scanf("%lld %lld %lld", &a, &b, &c)
#define sfuuu(a, b, c)     scanf("%llu %llu %llu", &a, &b, &c)
#define sfddd(a, b, c)     scanf("%lf %lf %lf", &a, &b, &c)

/**------- Printf----------*/
#define pf                 printf
#define pfig(a)            pf("%d ", a)
#define pfgap              pf(" ")
#define pfi(a)             printf("%d\n", a)
#define pfc(a)             printf("%c\n", a)
#define pfl(a)             printf("%lld\n", a)
#define pfu(a)             printf("%llu\n", a)
#define pfs(a)             printf("%s\n", a)
#define pfd(a)             printf("%.2lf\n", a)
#define pfii(a, b)         printf("%d %d\n", a, b)
#define pfll(a, b)         printf("%lld %lld\n", a, b)
#define pfuu(a, b)         printf("%llu %llu\n", a, b)
#define pfdd(a, b)         printf("%.2lf %.2lf\n", a, b)
#define pfiii(a, b, c)     printf("%d %d %d\n", a, b, c)
#define pflll(a, b, c)     printf("%lld %lld %lld\n", a, b, c)
#define pfuuu(a, b, c)     printf("%llu %llu %llu\n", a, b, c)
#define pfddd(a, b, c)     printf("%.2lf %.2lf %.2lf\n", a, b, c)
#define pnl                printf("\n")

/**--------File------------*/
#define output             freopen("output.txt","w",stdout)
#define input              freopen("input.txt","r",stdin)
#define inOut              input; output
#define Case               printf("Case %d: ", cases)
#define Casepp             cout << "Case " << cases << ": "

/**--------Constant------------*/
#define mx2                101
#define mx3                1001
#define mx4                10001
#define mx5                100001
#define mx6                1000001
#define INF                0x3f3f3f3f
#define eps                1e-8

/**--------Loops--------------*/
#define frab(i, a, b)      for(__typeof(b) i=(a); i<=(b); i++)
#define fr0(i, n)          frab(i, 0, n-1)
#define fr1(i, n)          frab(i, 1, n)
#define rfrab(i, a, b)     for(__typeof(b) i=(b); i>=a; i--)
#define rfr0(i, n)         rfrab(i, (n)-1, 0)
#define rfr1(i, n)         rfrab(i, n, 1)
#define frabv(i, a, b, v)  for(__typeof(b) i=(a); i<=(b); i+=v)
#define rfrabv(i, a, b, v) for(__typeof(b) i=(b); i>=a; i-=v)
#define frstl(i, s)        for(__typeof((s).end()) i=(s).begin(); i != (s).end(); i++)

/**-------Upper & Lower Bound-------*/
#define LB(a, v)            (lower_bound(all(a), v))
#define UB(a, v)            (upper_bound(all(a), v))

/**--------DeBug------------*/
#define watch(x)            cout<<(#x)<<" is "<<x<<"\n"
#define chk                 cout<<"Wtf"<<"\n"

const int mod = 1e9 + 7;
const int mx  = 2*mx5;

int main(){
    #define ONLINE_JUDGE
    #ifndef ONLINE_JUDGE
    inOut;
    #endif // ONLINE_JUDGE

    TestCases{
        ll x; sfi(x);
        bitset<30> bs;
        for(int i=29; i>=0; i--)
            if(x & (1<<i))
                bs.set(i);

        for(int i=0; i<30; i++)
        if(!bs.test(i)){
            bs.set(i);
            break;
        }

        ll ans = 0;
        for(int i=0; i<30; i++)
            if(bs.test(i))
                ans |= (1<<i);
        pfl(ans);
    }

    return 0;
}
