# 1부터 N까지 자연수 중에서 '중복없이'(visited 써야겠지?) / M 개를 고른 수열
def backtracking(lst, visited, result, target):
    # 기저조건
    global judge
    if len(result) == target:
        judge = 1
        for j in range(len(result)-1):
            if result[j] < result[j+1]:
                continue
            else:
                judge = 0
        if judge == 1:
            print(*result)
        return
    
    for i in range(len(lst)):
        if visited[i] == False:
            visited[i] = True
            result.append(lst[i])
            backtracking(lst, visited, result, target)
            visited[i] = False
            result.pop()


N, M = map(int, input().split())
lst = [x for x in range(1, N+1)]
visited = [False] * N
result = []
target = M
backtracking(lst, visited, result, target)