import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = int(input())
x = [0]
y = [0]
for i in range(num):
    info = list(map(int, input().split()))
    if info[0] == 0:
        x.append(info[1])
    elif info[0] == 1:
        y.append(info[1])
x.append(M)
y.append(N)
x.sort()
y.sort()
result = []
for i in range(len(x)-1):
    for j in range(len(y)-1):
        width = x[i+1] - x[i]
        height = y[j+1] - y[j]
        result.append(width*height)
print(max(result))