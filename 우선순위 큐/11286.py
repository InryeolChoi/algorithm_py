# 절댓값 힙
import sys
input = sys.stdin.readline
from heapq import *

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))
