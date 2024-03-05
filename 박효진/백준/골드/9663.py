def backtracking(i, j, arr, visited, result, target, cnt):

    total = 0
    for i in range(len(arr)):
        total += sum(arr[i])
    if total == target:
        cnt += 1
        return cnt
    dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    for k in range(9):
        for l in range(len(arr)):
            if 0 <= i+dx[k]*l < N and 0 <= j+dy[k]*l < N and visited[i+dx[k]*l][j+dy[k]*l] == False:
                visited[i+dx[k]*l][j+dy[k]*l] = True
                result.append(arr[i+dx[k]*l][j+dy[k]*l])
                backtracking(i, j, arr, visited, result, target,cnt)
                visited[i+dx[k]*l][j+dy[k]*l] = False
                result.pop()
            else:
                return

N = int(input())
arr = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = []
target = N
cnt = 0
for i in range(N):
    for j in range(N):
        print(backtracking(i, j, arr, visited, result, target, cnt))
