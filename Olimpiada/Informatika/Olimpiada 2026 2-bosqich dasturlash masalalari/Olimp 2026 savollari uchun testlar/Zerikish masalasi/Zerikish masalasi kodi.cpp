#include <bits/stdc++.h>

using namespace std;
using ll = long long;
int cnt[100100];
ll dp[100100];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n; cin >> n;
	int x;
	for(int i = 0; i < n; i++){
		cin >> x;
		cnt[x]++;
	}
	dp[0] = 0;
	dp[1] = cnt[1];
	for(int i = 2; i <= 1e5; i++){
		dp[i] = max(dp[i - 1], 1LL * cnt[i] * i + dp[i - 2]);
	}
	cout << dp[100000];
}
