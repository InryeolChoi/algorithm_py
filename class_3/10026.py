"""적록색약"""
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count1, count2 = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, color):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == False: 
            visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == color:
                    queue.append([nx, ny])
                    

# 정상인 경우              
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j, graph[i][j])
            count1 += 1
print(count1, end = " ")

# 색약인 경우
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j, graph[i][j])
            count2 += 1
print(count2)