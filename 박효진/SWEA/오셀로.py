T = int(input().strip())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    arr[N//2][N//2] = arr[N//2 + 1][N//2 + 1] = 2   #백
    arr[N//2][N//2 +1] = arr[N//2 + 1][N//2] = 1   #흑

    for _ in range(M):
        x, y, info = map(int, input().split())
        di = [0, 1, 1, 1, 0, -1, -1, -1]
        dj = [1, 1, 0, -1, -1, -1, 0, 1]
        arr[x][y] = info
        for k in range(8):
            stack = []

            for l in range(1, N+1):
                if 0 <= x+di[k]*l < N+1 and 0 <= y+dj[k]*l < N+1:
                    stack.append([x+di[k]*l, y+dj[k]*l])
                    if arr[x+di[k]*l][y+dj[k]*l] == info:
                        for p, q in stack:
                            arr[p][q] = info
                        break
                    elif arr[x+di[k]][y+dj[k]] == 0:
                        break
    bk = 0
    wht = 0
    for cn in arr:
        bk += cn.count(1)
        wht += cn.count(2)
    print(f'#{tc}', bk, wht)