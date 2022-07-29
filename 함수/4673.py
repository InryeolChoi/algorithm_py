"""셀프 넘버"""
def d(n):
    n = n + sum(map(int, str(n)))
    return n
notselfnum = set()

for n in range(10000):
    notselfnum.add(d(n))

for i in range(10000):
    if i not in notselfnum:
        print(i)