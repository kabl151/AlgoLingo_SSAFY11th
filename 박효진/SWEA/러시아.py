T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    lst = []
    result = []
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                if i+j+k == N:
                    lst.append([i,j,k])
    for i in range(len(lst)):
        cnt = 0
        w_line = ['W'] + [lst[i][0]]
        b_line = ['B'] + [lst[i][1]]
        r_line = ['R'] + [lst[i][2]]
        for j in range(w_line[1]):
            for l in range(M):
                arr[j][l] != w_line[0]
                cnt += 1
        for j in range(w_line[1], w_line[1] + b_line[1]):
            for l in range(M):
                arr[j][l] != b_line[0]
                cnt += 1
        for j in range(w_line[1] + b_line[1], w_line[1] + b_line[1] + r_line[1]):
            for l in range(M):
                arr[j][l] != r_line[0]
                cnt += 1
        result.append(cnt)
    print(f'#{tc}', min(result))