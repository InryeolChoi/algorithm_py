"""이중 우선순위 큐"""
import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    max_heap = [] # 최댓값 힙
    min_heap = [] # 최솟값 힙
    n = int(input())
    visited = [0] * n # 체크용 배열

    for i in range(n):
        order, data = input().split()
        
        # 데이터 넣기
        if order == 'I':
            heapq.heappush(min_heap, (int(data), i))
            heapq.heappush(max_heap, (-int(data), i))
            visited[i] = 1

        # 최댓값 꺼내기
        elif order == 'D' and data == '1':
            # 이미 제거된 정수 제거
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)

            # 최댓값 삭제
            if max_heap:
                visited[max_heap[0][1]] = 0
                heapq.heappop(max_heap)

            
        # 최솟값 꺼내기
        elif order == 'D' and data == '-1':
            # 이미 제거된 정수 제거
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)

            # 최솟값 삭제
            if min_heap:
                visited[min_heap[0][1]] = 0
                heapq.heappop(min_heap)

    if 1 not in visited:
        print("EMPTY")
    else:
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

        print(-max_heap[0][0], min_heap[0][0])