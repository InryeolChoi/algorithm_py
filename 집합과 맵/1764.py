""" 듣보잡 """

n, m = map(int, input().split())
x = set([input() for _ in range(n)]) # 듣도 못한 사람
y = set([input() for _ in range(m)]) # 보도 못한 사람

xy = sorted(list(x.intersection(y)))
print(len(xy))
for i in xy: print(i)