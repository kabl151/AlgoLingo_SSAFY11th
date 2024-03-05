N, M = map(int, input().split())
empty_arr = [[0]*(M+2) for _ in range(N+2)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    empty_arr[i] = [0] + arr + [0]
    mid_num = 0
    total_num = 0
    max_num = 0
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            mid_num = empty_arr[j][k]
            for l in range(4):
                total_num += empty_arr[j+dx[l]][k+dy[l]] + mid_num
                if total_num >= max_num:
                    max_num = total_num
    print(max_num)