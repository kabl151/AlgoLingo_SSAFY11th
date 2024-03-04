import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*101 for _ in range(101)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]
length = 0
for i in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k] = 1
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for k in range(4):
                if arr[i+dx[k]][j+dy[k]] == 0:
                    length += 1
print(length)