"""파도반 수열"""
# 소라모양 도형에서 규칙 찾기

x = [0] * 200
x[1], x[2], x[3] = 1, 1, 1

def P(n):
    if n > 3:
        for i in range(4, n+1):
            x[i] = x[i-3] + x[i-2]
    return print(x[n])

for _ in range(int(input())):
    P(int(input()))