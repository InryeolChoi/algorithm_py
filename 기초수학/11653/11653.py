import sys
input = sys.stdin.readline

n = int(input())
d = 2
while True:
    if n == 1:
        break
    if n % d == 0:
        n //= d
        print(d)
    else:
        d += 1
