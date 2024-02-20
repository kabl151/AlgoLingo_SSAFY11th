def judgement():
    global result
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    for l in range(1,5):
                        nx = i+dx[k]*l
                        ny = j+dy[k]*l
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                            cnt +=1
                        else:
                            break
                    if cnt == 5:
                        result = 1
                        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    result = 0
    judgement()
    if result == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')