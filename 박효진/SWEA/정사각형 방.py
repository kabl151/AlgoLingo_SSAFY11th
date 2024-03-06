def search(i,j):
    global cnt
    for k in range(4):
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N and arr[i+dx[k]][j+dy[k]] == arr[i][j] + 1:
            path.append(arr[i+dx[k]][j+dy[k]])
            cnt += 1
            search(i+dx[k],j+dy[k])
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_cnt = -1
    max_place = [[0,0]]
    path = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            search(i,j)
            if max_cnt < cnt:
                max_cnt = cnt
                max_place.pop()
                max_place.append([i,j])
            elif max_cnt == cnt:
                if arr[max_place[0][0]][max_place[0][1]] > arr[i][j]:
                    max_place.pop()
                    max_place.append([i,j])
    print(f'#{tc}', arr[max_place[0][0]][max_place[0][1]], max_cnt)