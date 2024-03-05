fn = list(map(int,input().split()))
c = int(input())
n0 = int(input())

if fn[0]*n0 + fn[1] <= c * n0 and c >= fn[0]:
    print(1)
else:
    print(0)