#백준 16395번
#실버5
#2026-01-07

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[1]*k for k in range(1, n+1)]

for i in range(1, n):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][k-1])


    

