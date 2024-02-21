T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt_lst = [0]*5001
    for i in range(N):
        A, B = map(int, input().split())
        for k in range(A, B+1):
            cnt_lst[k] += 1
    result = []
    P = int(input())
    C_lst = []
    for j in range(P):
        C_lst.append(int(input()))
    for l in C_lst:
        result.append(cnt_lst[l])
    print(f'#{tc}', *result)