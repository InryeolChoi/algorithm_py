"""미로 탐색"""
from collections import deque

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 가로와 세로 확인
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            # 값이 0인 경우
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문한 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

                # for i in range(n):
                #     print(graph[i])
                # print("\n")
    # print("\n")
    return graph[n-1][m-1]

# for i in range(n):
#     print(graph[i])
print(bfs(0, 0))
