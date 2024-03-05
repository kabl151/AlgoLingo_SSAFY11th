import sys
input = sys.stdin.readline

N = int(input())
result = []
a = N // 5
b = N % 5
while a != -1:
    if b == 0:
        result.append(a)
        break
    elif b != 0 and b % 3 == 0:
        c = b // 3
        result.append(a + c)
        break
    a = a - 1
    b = b + 5
if len(result) == 0:
    print(-1)
else:
    print(*result)