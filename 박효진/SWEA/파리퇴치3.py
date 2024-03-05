T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가로 세로 case1
    da = [0, 1, 0, -1]
    db = [1, 0, -1, 0]
    # 좌대각 우대각 case2
    dc = [-1, 1, 1, -1]
    dd = [1, 1, -1, -1]
    result = []
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            total_kill_1 = now
            total_kill_2 = now
            for k in range(4):
                for l in range(1, M):
                    na = i+da[k]*l
                    nb = j+db[k]*l
                    if 0 <= na < N and 0 <= nb < N:
                        total_kill_1 += arr[na][nb]
                    nc = i+dc[k]*l
                    nd = j+dd[k]*l
                    if 0 <= nc < N and 0 <= nd < N:
                        total_kill_2 += arr[nc][nd]
            result.append(total_kill_1)
            result.append(total_kill_2)
    print(f'#{tc}', max(result))