N, M = list((map(int,input().split())))

if N == 1 and M == 1:
    print(0)
else:
    print(N + M - 1)