def backtracking(lst, visited, result, target):
    if len(result) == target:
        print(*result)
        return
    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            result.append(lst[i])
            backtracking(lst, visited, result, target)
            visited[i] = False
            result.pop()

N, M = map(int, input().split())
lst = [x for x in range(1, N+1)]
visited = [False]*N
result = []
target = M
backtracking(lst, visited, result, target)