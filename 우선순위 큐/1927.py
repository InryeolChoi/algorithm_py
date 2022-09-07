# 최소 힙
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
            print(heappop(heap))
    elif x != 0:
        heappush(heap, x)
