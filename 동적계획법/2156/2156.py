## 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0]
dp.append(wine[1])
if n > 1:
    dp.append(wine[1] + wine[2])

for i in range(3, n + 1):
    a = dp[i-1] 
    b = dp[i-2] + wine[i]
    c = dp[i-3] + wine[i] + wine[i-1]
    dp.append(max(a, b, c))

print(dp[n])