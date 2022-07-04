"""구간 합"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
cumsum = [data[0]] + [None] * (n-1)

for i in range(1, n):
    cumsum[i] = data[i] + cumsum[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(cumsum[b-1])
    else:
        print(cumsum[b-1] - cumsum[a-2])