"""별 찍기 - 10"""

def star(i, j , num):
    if (i//num) % 3 == 1 & (j//num) % 3 == 1:
        print(" ", end="")

    else:
        if num//3 == 0:
            print("*", end="")
        else:
            star(i, j, num//3)

n = int(input())
for i in range(n):
    for j in range(n):
        star(i, j, n)
    print("\n")
