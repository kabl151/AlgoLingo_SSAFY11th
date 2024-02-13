T = int(input())
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
            if arr[x+di[k]][y+dj[k]] == info or arr[x+di[k]][y+dj[k]] == 0:
                continue
            else:
                for l in range(N):
                    if arr[x+di[k]*l][y+dj[k]*l] != 0:
                        stack.append([x+di[k]*l, y+dj[k]*l])
                        if arr[x+di[k]*l][y+dj[k]*l] == info:
                            for p, q in stack:
                                arr[p][q] = info
                            break
                        
    black = 0
    white = 0
    for i in arr:
        black += i.count(1)
        white += i.count(2)
    print(f'#{tc}', black, white)