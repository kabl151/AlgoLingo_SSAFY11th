import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
height = 0

cnt = 0
while height <= V:
    cnt += 1
    height += A
    if height >= V:
        break
    height -= B
print(cnt)