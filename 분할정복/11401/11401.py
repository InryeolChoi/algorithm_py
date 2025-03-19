""" 이항계수 3 """
import sys
input = sys.stdin.readline

# 팩토리얼
def fac(n):
    global p
    x = 1
    for i in range(2, n+1):
        x = (x * i) % p
    return x

# 거듭제곱
def square(n, k):
    global p
    if k == 0:
        return 1
    elif k == 1:
        return n

    temp = square(n, k//2)
    if k % 2 == 0:
        return temp * temp % p
    else:
        return temp * temp * n % p


if __name__ == "__main__":
    n, k = map(int, input().split())
    p = 1000000007

    # 분모
    top = fac(n)

    # 분자
    bottom = fac(k) * fac(n-k) % p

    # 전체 계산
    print( top * square(bottom, p-2) % p )