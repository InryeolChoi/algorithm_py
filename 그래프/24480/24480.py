"""알고리즘 수업 - 깊이 우선 탐색 2"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(n, graph, visited):
    global cnt 
    visited[v] = True
    order[v] = cnt
    for i in graph[n]:
        if i not in visited:
            visited[i] = True
            order[i] = cnt
            cnt += 1
            dfs(i, graph, visited)
        

n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort(reverse=True)



visited = [False for _ in range(n+1)]
order = [0 for _ in range(n+1)]
cnt = 0
dfs(graph, r, visited)
for i in range(len(order)):
    print(order[i])