import sys
input = sys.stdin.readline

block = [[0]*100 for _ in range(100)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            block[j][k] = 1

cnt = 0
for k in range(100):
    cnt += sum(block[k])

print(cnt)