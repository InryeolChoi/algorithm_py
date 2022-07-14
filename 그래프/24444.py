"""알고리즘 수업 - 너비 우선 탐색 1"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start):
    global cnt
    queue = deque([start])
    visited[start] = True
    order[start] = cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
                order[i] = cnt

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

visited = [False] * (n+1)
order = [0] * (n+1)
cnt = 1
bfs(graph, r)
for i in order[1::]:
    print(i)