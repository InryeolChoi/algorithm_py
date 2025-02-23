"""골드바흐의 추측"""

# 소수 집합
def find_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(0.5)) + 1):
        if x % i == 0:
            return False
    return True

primes = []
for i in range(1, 10000):
    if find_prime(i):
        primes.append(i)

# 골드바흐 수 출력
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(n//2, 0, -1):
        if i in primes and n-i in primes:
            print(i, n-i)
            break
