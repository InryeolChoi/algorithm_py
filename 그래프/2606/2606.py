"""바이러스"""
import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 번호쌍의 수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, graph, visited):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph, visited)

visited = []
dfs(1, graph, visited)
print(len(visited)-1)