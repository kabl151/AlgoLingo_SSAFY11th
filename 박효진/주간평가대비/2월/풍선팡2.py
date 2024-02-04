T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    pos_nun = 0
    total_num = 0
    for i in range(N):
        for j in range(M):
            pos_num = arr[i][j]
            

            pass