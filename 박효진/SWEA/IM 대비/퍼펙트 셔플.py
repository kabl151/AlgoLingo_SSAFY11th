T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    suf_lst = []
    if N % 2 == 0:
        for i in range(N//2):
            suf_lst.append(arr[i])
            suf_lst.append(arr[i+N//2])
    else:
        for i in range(N//2):
            suf_lst.append(arr[i])
            suf_lst.append(arr[i+N//2+1])
        suf_lst.append(arr[N//2])
    print(f'#{tc}', *suf_lst)