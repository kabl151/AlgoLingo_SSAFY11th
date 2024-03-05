import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []
    result = []
    cnt = 0
    for idx in range(N):
        lst.append([arr[idx],idx])
    dq = deque(lst)
    while dq:
        max_num = max(dq)
        if max_num[0] == dq[0][0]:
            cnt += 1
            dq[0] += [cnt]
            result.append(dq.popleft())
        else:
            dq.rotate(-1)

    for i in result:
        if i[1] == M:
            print(i[2])
            break