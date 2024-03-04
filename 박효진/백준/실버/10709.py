import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = [list(map(str, input())) for _ in range(H)]
cloud = [[-1]* W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            cloud[i][j] = 0
for i in range(H):
    for j in range(W):
        cnt = 0
        if cloud[i][j] == 0:
            for k in range(j+1, W):
                cnt += 1
                if cloud[i][k] == -1:
                    cloud[i][k] = cnt
                elif cloud[i][k] == 0:
                    break
for i in range(H):
    print(*cloud[i])