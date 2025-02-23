# bfs
"""단자번호붙이기"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph, village = [], []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            village.append(count)

print(len(village))
for v in village:
    print(v)