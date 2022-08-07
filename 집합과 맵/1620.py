""" 포켓몬 마스터 이다솜 """

n, m = map(int, input().split())
data = [input() for _ in range(n)]
num = [str(i) for i in range(1, len(data)+1)]

pokedex = dict(zip(num, data))
pokedex2 = {v:k for k,v in pokedex.items()}
# value -> key 상황을 위해 뒤집힌 도감 생성

aim = [input() for _ in range(m)]

for t in aim:
    if t.isdigit() == True:
        print(pokedex[t])
    else:
        print(pokedex2[t])
