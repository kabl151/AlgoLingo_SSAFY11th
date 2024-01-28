n = int(input())
a, b = map(int, input().split())
if n < a // 2 + b:
    print(n)
else :
    print(a // 2 + b)