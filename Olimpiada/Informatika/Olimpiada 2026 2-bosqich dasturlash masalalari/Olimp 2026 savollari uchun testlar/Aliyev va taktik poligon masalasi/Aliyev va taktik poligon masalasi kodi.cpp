#include <bits/stdc++.h>
using namespace std;
using ll = long long;
 
vector<int>cats;
vector<vector<int>> arr;
int res = 0, n, m;
 
void dfs(int node, int parent, int cnt_cats){
	if(cats[node-1]) cnt_cats++;
	else cnt_cats = 0;
	
	if(cnt_cats > m) return;
	bool isLeaf = true;
	for(int temp : arr[node]){
		if(temp != parent){
			isLeaf = false;
			dfs(temp, node, cnt_cats);
		}
	}
	if(isLeaf) res++;
}
 
int main()
{
	freopen("testlar/0010.in", "r", stdin);
	freopen("testlar/0010.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	cats.resize(n);
	arr.resize(n + 1);
	for(int i = 0; i < n; i++) cin >> cats[i];
	for(int i = 0; i < n - 1; i++){
		int x, y;
		cin >> x >> y;
		arr[x].push_back(y);
		arr[y].push_back(x);
	}
	
	dfs(1, 0, 0);
	cout << res;
}
 
