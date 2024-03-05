import sys
input = sys.stdin.readline

def fibo(n):
    global cnt_1
    global cnt_0
    if n == 1:
        cnt_1 += 1
        return 1
    elif n == 0:
        cnt_0 += 1
        return 1
    return fibo(n-1) + fibo(n-2)

T = int(input())
for i in range(T):
    cnt_1 = 0
    cnt_0 = 0
    n = int(input())
    fibo(n)
    print(cnt_0, cnt_1)