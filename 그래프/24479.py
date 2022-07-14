"""알고리즘 수업 - 깊이 우선 탐색 1"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt 
    visited[v] = True
    order[v] = cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort(reverse=True)

visited = [False] * (n+1)
order = [0] * (n+1)
cnt = 1

dfs(graph, r, visited)
for i in range(1, len(order)):
    print(order[i])