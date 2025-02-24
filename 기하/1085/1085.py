"""직사각형에서 탈출하기"""

x, y, w, h = map(int, input().split())
print(min(x, y, w-h, h-y))