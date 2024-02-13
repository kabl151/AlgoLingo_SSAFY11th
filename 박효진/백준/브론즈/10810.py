import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0]* N
for _ in range(M):
    i, j, num = map(int, input().split())
    for x in range(i-1,j):
        arr[x] = num
print(*arr)