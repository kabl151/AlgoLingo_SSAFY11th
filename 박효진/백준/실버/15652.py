def backtracking(lst, result, target):
    if len(result) == target:
        judge = 1
        for j in range(len(result)-1):
            if result[j] <= result[j+1]:
                continue
            else:
                judge = 0
        if judge == 1:
            print(*result)
        return

    for i in range(len(lst)):
        result.append(lst[i])
        backtracking(lst, result, target)
        result.pop()

N, M = map(int, input().split())
lst = [x for x in range(1, N+1)]
result = []
target = M
backtracking(lst, result, target)