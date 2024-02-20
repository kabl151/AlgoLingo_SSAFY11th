T = 10
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input()))for _ in range(100)]
    # start, end 좌표 찾기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                x = i
                y = j
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False]*100 for _ in range(100)]
    #함수 정의
    def BFS(x,y):   # 시작지점
        queue = []
        queue.append([x,y])
        visited[x][y] = True
        while queue:
            x,y = queue.pop(0)
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                elif nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 3:
                    return 1
        return 0

    #함수 호출
    print(f'#{tc}', BFS(x,y))
