T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(100):
        for j in range(100):
            now = arr[i][j]
            if now == 1:
                for k in range(1, 100-i):
                    if arr[i+k][j] == 0:
                        continue
                    elif arr[i+k][j] == 1:
                        break
                    elif arr[i+k][j] == 2:
                        cnt += 1
                        break
    print(f'#{tc}', cnt)