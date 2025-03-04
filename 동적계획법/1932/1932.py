""" 정수 삼각형 """
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(x[i])):
        if j == 0:
            x[i][j] = x[i][j] + x[i-1][j]
        elif j == len(x[i])-1:
            x[i][j] = x[i][j] + x[i-1][j-1]
        else:
            x[i][j] = x[i][j] + max(x[i-1][j-1], x[i-1][j])

print(max(x[n-1]))