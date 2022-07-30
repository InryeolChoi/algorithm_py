"""소수 구하기"""
import math
import sys
input = sys.stdin.readline

def find_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    primes = 0
    if n == 0: break
    for i in range(n+1, (2*n) + 1):
        if find_prime(i):
            primes += 1
    print(primes)