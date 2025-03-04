"""2xn 타일링"""

import sys
input = sys.stdin.readline

n = int(input())
graph = [0 for _ in range(n+1)]
graph[0], graph[1] = 1, 2
for i in range(2, n+1):
		graph[i] = (graph[i-1] + graph[i-2]) % 10007

print(graph[n-1])