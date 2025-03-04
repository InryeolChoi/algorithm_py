"""알고리즘 수업 - 피보나치 수 1"""
# 동적계획법 vs 피보나치

def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

x = int(input())
print(fib(x), x-2)

"""
재귀함수: 모든 케이스를 다 계산해야 한다.
동적계획법: 딱 x-2번만 계산하면 된다.
"""
