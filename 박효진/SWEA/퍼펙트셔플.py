T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(str, input().split()))
    result = []
    if N % 2 == 0:
        for i in range(N//2):
            result.append(lst[i])
            result.append(lst[N//2 + i])

        print(f'#{tc}', *result)
    else:
        last = lst.pop(N//2)
        for i in range(N//2):
            result.append(lst[i])
            result.append(lst[N//2 + i])
        result.append(last)
       
        print(f'#{tc}', *result)