"""조합 0의 갯수"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def cnt(a, b):
    count = 0
    while a:
        a //= b
        count += a
    return count

count2 = cnt(n, 2) - cnt(n-m, 2) - cnt(m, 2)
count5 = cnt(n, 5) - cnt(n-m, 5) - cnt(m, 5)
print(min(count2, count5))