"""블랙잭"""

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answers = []
for i in range():
    for j in range(i+1, n+1):
        for k in range(j+1, n):
            num = cards[i] + cards[j] + cards[k]
            if num <= m:
                answers.append(num)
print(max(answers))