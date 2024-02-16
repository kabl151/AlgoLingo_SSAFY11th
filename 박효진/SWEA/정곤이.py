T = int(input())
for tc in range(1, T+1):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    lst = []
    result = []
    for i in range(N):
        for j in range(i+1, N):
            lst.append(str(arr[i] * arr[j]))
    for i in range(len(lst)):
        if len(lst[i]) == 1:
            result.append(int(lst[i]))
        else:
            result_num = 1
            for j in range(len(lst[i])-1):
                if int(lst[i][j]) <= int(lst[i][j+1]):
                    continue
                else:
                    result_num = 0
            if result_num == 1:
                result.append(int(lst[i]))
    if len(result) == 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', max(result))