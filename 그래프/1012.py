"""유기농 배추밭"""
# 세팅
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
count = 0

# dfs
def dfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0,  0, 1, -1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0 <= new_x < n) and (0 <= new_y < m):
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = -1
                dfs(graph, new_x, new_y)



for _ in range(int(input())):
    worm = 0
    # 그래프 입력
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # dfs로 분석
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(graph, i, j)
                worm += 1

    print(worm)