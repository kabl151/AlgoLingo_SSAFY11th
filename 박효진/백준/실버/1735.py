import sys
input = sys.stdin.readline

A_up, A_down = map(int, input().split())
B_up, B_down = map(int, input().split())
A = A_up*B_down+B_up*A_down
B = A_down*B_down
lst = [A, B]
gcd = 0
# 최대공약수(GCD)를 구해서 위아래 모두 나눠주기
if A >= B:
    while True:
        r = A % B
        if r == 0:
            gcd = B
            break
        else:
            A = B
            B = r
else:
    A, B = B, A
    while True:
        r = A % B
        if r == 0:
            gcd = B
            break
        else:
            A = B
            B = r
print(lst[0]//gcd, lst[1]//gcd)