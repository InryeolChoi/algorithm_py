""" 숨바꼭질 """
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0] * 1000001

def find(start):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 1000000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

print(find(n))



