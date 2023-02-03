"""연결 요소의 갯수"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start, depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


n, m = map(int, input().split())
graph = [[] * (n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i, 0)
            count += 1

print(count)