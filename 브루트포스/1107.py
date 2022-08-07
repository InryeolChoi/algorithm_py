"""리모콘"""
import sys
input = sys.stdin.readline

aim_ch = int(input())
malfunc = int(input())

if malfunc != 0:
    malfunc_list = list(input().split())
else:
    malfunc_list = []

# 1번 방안
ans = abs(aim_ch - 100)

# 2번 방안
for i in range(1000001):
    count = 0
    for num in str(i):
        if num in malfunc_list:
            count += 1

		# 1번 vs 2번 방안 계속 비교
    if count == 0:
        ans = min(ans, abs(aim_ch - i) + len(str(i)))

print(ans)