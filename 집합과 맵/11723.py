import sys

S = set()
n = int(input())
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    
    if len(order) == 1:
        if order[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue

    function, x = order[0], int(order[1])
    if function == "add":
        S.add(x)
    elif function == "remove":
        S.discard(x)

    elif function == "check":
        print(1 if x in S else 0)
    elif function == "toggle":
        if x in S: 
            S.discard(x)
        else:
            S.add(x)
