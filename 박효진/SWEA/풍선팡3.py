T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pang_lst = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            mid_num = arr[i][j]
            total_num = mid_num
            for k in range(4):
                for l in range(1,mid_num+1):
                    nx = i + dx[k]*l
                    ny = j + dy[k]*l
                    if 0 <= nx < N and 0 <= ny < N:
                        total_num += arr[nx][ny]
            pang_lst.append(total_num)
    print(f'#{tc}',max(pang_lst)-min(pang_lst))