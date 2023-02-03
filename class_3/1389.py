""" 케빈 베이컨의 6단계 법칙 """
import sys
input = sys.stdin.readline
from collections import deque

# bfs 탐색
def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        target = queue.popleft()
        
        # 친구관계 탐색: 탐색 안된 친구라면 탐색.
        for i in graph[target]:
            if not visited[i]:
                # 탐색하기 위한 횟수 체크
                visited[i] = visited[target] + 1
                queue.append(i)

# 그래프 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수
result = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result) + 1))