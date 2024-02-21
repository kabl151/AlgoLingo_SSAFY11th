def bfs_miro(x,y,miro,result,target):
    result.append([x,y])
    if miro[x][y] == 0:
        miro[x][y] = 1
    elif miro[x][y] == target:
        return 1
    while result != 0:
        for i in range(4):
            if miro[x+dx[i]][y+dy[i]] == 0:
                # result.append([x+dx[i],y+dy[i]])
                bfs_miro(x+dx[i],y+dy[i],miro,result,target)
                result.pop()


T = int(input())
for tc in range(1, T+1):
    miro = [list(map(int, input())) for _ in range(16)]
    start_idx_x = 1
    start_idx_y = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = []
    target = 3
    print(bfs_miro(start_idx_x,start_idx_y,miro,result,target))
