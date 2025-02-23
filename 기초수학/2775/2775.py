"""부녀회장이 될테야"""
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [([1] + [0] * (n)) for i in range(k+2)]
    arr[0] = [i for i in range(1, n+2)]

    for i in range(1, k+2):
        for j in range(n+1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[k][n-1])