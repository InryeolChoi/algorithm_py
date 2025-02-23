"""DFS와 BFS"""
from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    for e in graph[start]:
        if not visited[e]:
            dfs(graph, e, visited)



def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end=' ')

        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

visited_1, visited_2 = [False] * (n+1), [False] * (n+1)
dfs(graph, r, visited_1)
print("")
bfs(graph, r, visited_2)