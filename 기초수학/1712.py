"""손익분기점"""

a, b, c = map(int, input().split())
if c <= b:
    print(-1)
else:
    answer = (-a // (b-c)) + 1
    print(answer)