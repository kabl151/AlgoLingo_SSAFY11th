# 중복이가능하기 때문에 visited는 필요없겠지??
def backtracking(lst,result,target):
    if len(result) == target:
        print(*result)
        return
    for i in range(len(lst)):
        result.append(lst[i])
        backtracking(lst,result,target)
        result.pop()

N, M = map(int, input().split())
lst = [x for x in range(1, N+1)]
result = []
target = M
backtracking(lst,result,target)