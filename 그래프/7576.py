"""토마토"""
import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 큐 구현
queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])    
        # 토마토가 있는 모든 지역에서 동시에 뻗어감.
        # 익은 토마토가 있는 모든 지역을 미리 넣어야 함.
        # 기존에 1인 애들 -> 새로 추가된 애들 순으로 빠져나오게 됨.

# bfs() 구현
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1
bfs()

# 최대 일수 구하기
flag = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = True
            break
if flag:
    print(-1)
else:
    print( max(map(max, graph)) - 1)