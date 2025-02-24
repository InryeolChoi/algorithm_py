""" RGB거리 """
# 동적 계획법 이용

n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    x[i][0] = x[i][0] + min(x[i-1][1], x[i-1][2])
    x[i][1] = x[i][1] + min(x[i-1][0], x[i-1][2])
    x[i][2] = x[i][2] + min(x[i-1][0], x[i-1][1])

print(min(x[n-1]))