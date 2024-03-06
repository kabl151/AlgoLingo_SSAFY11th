def permutation(n):
    global min_num
    if len(path) != 0 and path[0] != 0:
        return
    if n == N:
        sum_num = 0
        path.append(0)
        for i in range(n):
            sum_num += arr[path[i]][path[i+1]]
        if sum_num < min_num:
            min_num = sum_num
        path.pop()
        return
    for i in range(N):
        if used[i] == False:
            used[i] = True
            path.append(i)
            permutation(n+1)
            path.pop()
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    min_num = 100*10*10
    used = [False] * (N+1)
    permutation(0)
    print(f'#{tc}', min_num)