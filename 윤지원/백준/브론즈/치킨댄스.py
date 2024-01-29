N = int(input())
a, b = map(int,input().split())

cnt = a//2 + b//1
if cnt <= N:
    print(cnt)
else:
    print(N)