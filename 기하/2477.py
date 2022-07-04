""" 참외밭 """
import sys
input = sys.stdin.readline

# 입력
n = int(input())
arr = []
for i in range(6):
    direction, length = map(int, input().split())
    arr.append(length)

# 최대 넓이 구하기
max = 0
min = 0
for i in range(6):
    temp = arr[i] * arr[(i+1)%6]
    if max < temp:
        max = temp
        idx = i
min = arr[(idx + 3) % 6] * arr[(idx + 4) % 6]
print((max - min) * n)

