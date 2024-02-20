from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    piz_lst = list(map(int, input().split()))
    idx = 0 # 피자인덱스
    dq = deque()
    for i in range(N):
        dq.append([idx, piz_lst[idx]])
        idx += 1
    while len(dq) != 1:
        if len(dq) == 1:
            break
        dq[0][1] = dq[0][1] // 2
        if dq[0][1] == 0 and idx <= M - 1:
            dq[0] = [idx,piz_lst[idx]]
            idx += 1
        if dq[0][1] == 0 and idx > M - 1:
            dq.popleft()
            dq[0][1] = dq[0][1] // 2
            if dq[0][1] == 0:
                continue
        dq.rotate(-1)
    print(f'#{tc}', dq[0][0]+1)