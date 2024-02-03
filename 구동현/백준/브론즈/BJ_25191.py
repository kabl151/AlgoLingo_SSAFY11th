c = int(input())
coke, beer = list(map(int,input().split()))

cnt = 0

cnt += coke //2
cnt += beer
if c > cnt:
    print(cnt)
else:
    print(c)