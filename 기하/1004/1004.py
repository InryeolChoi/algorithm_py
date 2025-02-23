"""어린왕자"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 시작점, 출발점 입력
    x1, y1, x2, y2 = map(int, input().split())

    # 행성 갯수 파악, 갯수세기용 변수 제작.
    n = int(input())
    count = 0

    # 각 행성들 입력
    for i in range(n):
        cx, cy, r = map(int, input().split())

    # 하나씩 꺼내며 보기
        d1 = (cx - x1)**2 + (cy - y1)**2 
        d2 = (cx - x2)**2 + (cy - y2)**2
        if d1 < r*r and d2 < r*r:
            pass
        elif d1 < r*r:
            count += 1
        elif d2 < r*r:
            count += 1

    print(count)