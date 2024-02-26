T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = []
    solve_wd = [0] + [1]*K + [0]
    stack = []
    for i in range(N+2):
        matrix += [[0]*(N+2)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i+1][j+1] = arr[i][j]
    dx = [0, 1]
    dy = [1, 0]
    result = 0
    for i in range(0, N+2):
        for j in range(0, N+2):
            if matrix[i][j] == 0:
                for k in range(2):
                    cnt = 0
                    for l in range(1,K+2):
                        nx = i+dx[k]*l
                        ny = j+dy[k]*l
                        if 0 <= nx <= N+1 and 0 <= ny <= N+1 and matrix[nx][ny] == 1:
                            cnt += 1
                        elif 0 <= nx <= N+1 and 0 <= ny <= N+1 and matrix[nx][ny] == 0:
                            break
                    if cnt == K:
                        result += 1
    print(f'#{tc}', result)