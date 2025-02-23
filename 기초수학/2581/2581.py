"""소수"""

m = int(input())
n = int(input())
sosu = []
for x in range(m, n+1):
    if x == 1:
        pass
    else:
        error = 0
        for u in range(2, x):
            if x % u == 0:
                error += 1
        if error == 0:
            sosu.append(x)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
