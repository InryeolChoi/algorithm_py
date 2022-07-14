"""비밀번호 찾기"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = dict()
for _ in range(n):
    ad, pw = input().split()
    dict[ad] = pw

for _ in range(m):
    addr = input().rstrip()
    print(dict[addr])