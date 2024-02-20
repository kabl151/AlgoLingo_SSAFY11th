def select(i, N, s):
    global min
    if i == N:
        if min > s:
            min = s
    elif s >= min:
        return
    else:
        for j in range(i, N):
            idx_lst[i], idx_lst[j] = idx_lst[j], idx_lst[i]
            select(i+1, N, s + arr[i][idx_lst[i]])
            idx_lst[i], idx_lst[j] = idx_lst[j], idx_lst[i]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx_lst = [x for x in range(N)]
    min = 90
    select(0, N, 0)
    print(f'#{tc} {min}')