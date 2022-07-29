"""ACM 호텔"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    # a 설정하기
    a = n % h
    if a == 0: a = h

    # b 설정하기
    if n % h == 0:
        b = n // h
    else: 
        b = (n // h) + 1

    # XX에 0 붙이기
    if b // 10 == 0: 
        b = str(0) + str(b)

    print("%d%s" % (a, b))