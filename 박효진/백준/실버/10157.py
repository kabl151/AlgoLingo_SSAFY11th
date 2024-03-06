import sys
input = sys.stdin.readline
C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
cnt = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr[R-1][0] = 1
x = R-1
y = 0
if C * R < K:
    print(0)
elif K == 1:
    print(1, 1)
else:
    while True:
        cnt += 1
        judge = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R  and 0 <= ny < C and arr[nx][ny] == 0:
                if i == 0 and 0 <= nx+1 < R and 0 <= ny -1 < C and arr[nx+1][ny-1] == 0:
                    nx = nx + 1
                    ny = ny - 1
                arr[nx][ny] = cnt
                x = nx
                y = ny
                if cnt == K:
                    print(y + 1, R - x)
                break
            else:
                judge += 1
        if judge == 4:
            break
