T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dok_lst = []
    for i in range(N):
        s, e = map(int, input().split())
        dok_lst.append([s,e])
    dok_lst.sort()
    cnt = 1
    compare = dok_lst[0]
    for i in range(N-1):
        if compare[1] <= dok_lst[i+1][0]:
            cnt += 1
            compare = dok_lst[i+1]
    print(f'#{tc}', cnt)