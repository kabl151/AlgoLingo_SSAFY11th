import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [[0]*(N+1) for _ in range(N+1)]
lst[1][1] = arr[0][0]
for i in range(1, N):
    lst[1][i+1] = lst[1][i] + arr[0][i]
for j in range(1, N):
    lst[j+1][1] = lst[j][1] + arr[j][0]
for i in range(1, N):
    for j in range(1, N):
        lst[i+1][j+1] = arr[i][j] + lst[i][j+1] + lst[i+1][j]- lst[i][j]
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(lst[x2][y2]-lst[x2][y1-1]-lst[x1-1][y2]+lst[x1-1][y1-1])