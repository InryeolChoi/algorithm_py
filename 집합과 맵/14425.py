""" 문자열 집합 """

n, m = map(int, input().split())
data = set([input() for _ in range(n)])
# 집합으로 묶는 것이 속도가 빨라지는 지름길.

cnt = 0
for _ in range(m):
    t = input()
    if t in data:
        cnt += 1
print(cnt)