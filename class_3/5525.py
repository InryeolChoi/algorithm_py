import sys
input = sys.stdin.readline

n = int(input()) # n
m = int(input()) # s의 길이
s = input()
i, count, answer = 0, 0, 0

while i < m-1 :
    if s[i:i+3] == "IOI":
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0
print(answer)