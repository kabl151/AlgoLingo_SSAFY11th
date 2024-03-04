import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]* 1002 for _ in range(1002)]
for i in range(1,N+1):
    x, y, width, height = map(int, input().split())
    for j in range(width):
        for k in range(height):
            arr[x+j][y+k] = i
for i in range(1,N+1):
    cnt = 0
    for j in range(1002):
        for k in range(1002):
            if arr[j][k] == i:
                cnt += 1
    print(cnt)