import sys
input = sys.stdin.readline
num = 1000000009

dp = [1, 2, 4]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n):
        dp.append(dp[i-1] % num + dp[i-2] % num + dp[i-3] % num)

    print(dp[n-1] % num)