T = int(input())
for tc in range(1, T+1):
    # 기본 데이터 생성
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 함수 정의
    def BFS(x,y):
        global arr
        queue = []
        queue.append([x,y])
        visited[x][y] = True
        if arr[x][y] == 3:
            return queue
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx >= 0 and nx < len(arr) and ny >= 0 and ny < len(arr[0]) and arr[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                elif nx >= 0 and nx < len(arr) and ny >= 0 and ny < len(arr[0]) and arr[nx][ny] == 3:
                    return visited[x][y] - 1
        return 0
    # 함수 호출 및 출력
    print(f'#{tc}',BFS(x,y))
