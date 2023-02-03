"""집합"""
import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    order = input().split()
    if len(order) == 1:
        ord1 = order[0]
    else:
        ord1, ord2 = order

        
    if ord1 == "add":
        S.add(int(ord2))

    elif ord1 == "remove":
        S.discard(int(ord2))

    elif ord1 == "check":
        if int(ord2) in S:
            print(1)
        else:
            print(0)

    elif ord1 == "toggle":
        if int(ord2) in S:
            S.discard(int(ord2))
        else:
            S.add(int(ord2))

    elif ord1 == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    else:
        S.clear()