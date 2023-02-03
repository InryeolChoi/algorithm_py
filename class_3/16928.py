"""뱀과 사다리 게임"""
import sys
input = sys.stdin.readline
from collections import deque

# 그래프 생성
graph = [0] * 101
visited  = [False] * 101

# 그래프 입력
n, m = map(int, input().split())
for _ in range(n): 
    a, b = map(int, input().split())
    graph[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = b

# 최단경로 찾기
def game(start, count):
    queue = deque()
    queue.append([start, count])
    while queue:
        location, cnt = queue.popleft()
        for i in range(1, 7):
            nx = location + i
            if nx == 100:   # 100인 경우 출력
                print(cnt + 1)
                return
            else: # 100이 아닌 경우
                while graph[nx] != 0:   # 사다리나 뱀인지 확인하기
                    nx = graph[nx]      # 점프한 자리로 이동
                if not visited[nx]:     # 가본적이 없으면 visited 바꾸기
                    queue.append([nx, cnt + 1]) # 큐에 넣어주기
                    visited[nx] = True
game(1, 0)