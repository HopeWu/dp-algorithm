#include <iostream>
#include <vector>
using namespace std;

int maximumProfit(int n, vector<int> &prices) {
    // add your logic here
	vector<int> dp(n+1, 0);
	dp[1] = prices[0];
	for(int i = 2; i <= n; i++){
		int _max = 0;
		for(int j = 1; j <= i; j++){
			if(_max < prices[j-1] + dp[i-j])
				_max = prices[j-1] + dp[i-j];
		}
		dp[i] = _max;
	}
	return dp[n];
}
