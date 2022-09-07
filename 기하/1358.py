"""하키"""
import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
count = 0
r = h//2

for _ in range(p):
    x_ex, y_ex = map(int, input().split())
    # 왼쪽 반원
    if x_ex < x:
        d1 = (x-x_ex)**2 + (y+r-y_ex)**2
        if d1 <= r*r:
            count += 1

    # 가운데 사각형
    elif x <= x_ex <= x+w:
        if y <= y_ex <= y+h:
            count += 1


    # 오른쪽 반원
    elif x+w < x_ex:
        d2 = (x+w-x_ex)**2 + (y+r-y_ex)**2
        if d2 <= r*r:
            count += 1

print(count)