"""계단 오르기"""
import sys
input = sys.stdin.readline

n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))
dp = [None] * n

for i in range(n):
    if i == 0:
        dp[i] = stair[i]
    elif i == 1:
        dp[i] = max(stair[i], stair[i] + stair[i-1])
    elif i == 2 :
        dp[i] = max(stair[i] + stair[i-2], stair[i] + stair[i-1])
    else:
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
print(dp[n-1])
