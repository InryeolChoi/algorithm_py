n, m = map(int, input().split())
data = list(map(int, input().split()))
for _ in range(m):
    i, j = map(int, input().split())
    sum1, sum2 = 0, 0
    for x in range(i-1):
        sum1 += data[x]
    for y in range(j):
        sum2 += data[y]
    print(sum2-sum1)