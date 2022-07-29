"""설탕 배달"""
n = int(input())
count = 0
while 1:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    else:
        count += 1
        n -= 3
        if n < 0:
            print(-1)
            break