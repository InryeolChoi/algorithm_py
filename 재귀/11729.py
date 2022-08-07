"""하노이 탑 이동 순서"""

def h_count(x):
    print(2**x-1)

def hanoi(n, start, via, end):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, end, via)
        print(start, end)
        hanoi(n-1, via, start, end) 

n = int(input())
h_count(n)
hanoi(n, 1, 2, 3)