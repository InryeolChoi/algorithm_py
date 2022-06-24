# 그리디 알고리즘
# 합을 최대로 만들기

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    # 괄호 안에는 전부 마이너스만!
    for j in s:
        cnt += int(j)
    num.append(cnt)
print(num)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
