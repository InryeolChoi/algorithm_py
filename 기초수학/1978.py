"""소수 찾기"""
n = int(input())
arr = list(map(int, input().split()))
sosu = 0

for a in arr:
    error = 0
    if a > 1:
        for x in range(2, a):
            if a % x == 0:
                error += 1
    if error == 0:
        sosu += 1
print(sosu)