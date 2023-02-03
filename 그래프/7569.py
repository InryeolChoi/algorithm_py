""" 토마토(3차원) """
import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 큐 구현
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((i, j, h))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    queue.append((nz, nx, ny))
bfs()

flag = False
answer = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                flag = True
            answer = max(answer, arr[i][j][k])

if flag:
    answer = -1
elif answer == 1:
    answer = 0
else:
    answer -= 1
print(answer)