import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_A = [list(map(int,input().split())) for _ in range(N)]
arr_B = [list(map(int,input().split())) for _ in range(N)]

new_arr = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        new_arr[i][j] = arr_A[i][j] + arr_B[i][j]

for k in range(N):
    print(*new_arr[k])