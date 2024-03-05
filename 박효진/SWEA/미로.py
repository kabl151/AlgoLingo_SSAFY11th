# #지나간 길은 -1로 표시해둘까?
'''
1
5
13101
10101
10101
10101
10021
'''

# T = int(input())
# N = int(input())
# miro_visited = [[False]*N for _ in range(N)]
# arr = [list(map(int, input())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 3:
#             si, sj = i, j
#         elif arr[i][j] == 2:
#             ei, ej = i, j

# def dfs(x,y):
#     print(x, y) # 현재 위치
#     miro_visited[x][y] = True
#     dx = [-1, 1, 0, 0] # 상 하 좌 우
#     dy = [0, 0, -1, 1]
#     for i in range(4):
#         nx, ny = x + dx[i], dy[i]
#         if nx >= 0 and nx < len(arr) and ny >= 0 and ny < len(arr[0]) and arr[nx][ny] == 0 and miro_visited[nx][ny] == False:
#             dfs(nx,ny)
#         elif arr[nx][ny] == arr[ei][ej]:
#             return print(1)

# dfs(si,sj)


#------------------------------------------------

T = int(input().rstrip())
for tc in range(1, T+1):
    N = int(input().rstrip())
    visited = [[False]*N for _ in range(N)]
    maze = [list(map(int, input().rstrip())) for _ in range(N)]
    result = 0
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                si, sj = i, j
            elif maze[i][j] == 2:
                ei, ej = i, j
    # DFS 함수 정의
    def DFS(x, y):
        global result
        global cnt
        # if visited [x][y] == 0: 
        #     cnt += 1
        visited[x][y] = True # 현재 위치를 방문 처리
        # 네 방향을 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0 and visited[nx][ny] == False:
                cnt +=1
                DFS(nx, ny) # DFS로 이동
            elif nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 2:
                result = 1
        return result

    DFS(si, sj)
    if result == 1:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc}', 0)