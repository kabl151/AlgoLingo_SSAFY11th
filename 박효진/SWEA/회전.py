from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dq = deque(map(int, input().split()))
    dq.rotate(-M)
    print(f'#{tc}', dq[0])