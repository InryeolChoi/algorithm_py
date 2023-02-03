""" 문자열 폭발 """
import sys
input = sys.stdin.readline

words = input().strip()
bomb = input().strip()
stack = []
lastchar = bomb[-1]
b = len(bomb)

for w in words:
    stack.append(w)
    if w == lastchar and "".join(stack[-b:]) == bomb:
        del stack[-b : ]

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))