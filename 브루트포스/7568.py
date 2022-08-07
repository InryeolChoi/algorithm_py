"""덩치"""
import sys
input = sys.stdin.readline


n = int(input())
score = [0] * n
weights, heights = [0] * n, [0] * n
for i in range(int(input())):
    weights[i], heights[i] = map(int, input().split()) 

flag = 0
for i in range(n):
    if weights[i] > weights[i-1]:
        if heights[i] > heights[i-1]:
            flag += 1
            score[i-1] += flag