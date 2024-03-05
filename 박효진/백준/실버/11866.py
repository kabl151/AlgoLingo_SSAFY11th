import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
lst = [x for x in range(1, N + 1)]
dq = deque(lst)
result = []
dq.rotate(-(K-1))
result.append(dq.popleft())
for i in range(N-1):
    dq.rotate(-(K-1))
    result.append(dq.popleft())
if len(dq) != 0:
    result.append(dq.popleft())
result_wd = ''
for i in range(len(result) - 1):
    result_wd += str(result[i]) + ', '
result_wd += str(result[-1])
print('<'+result_wd+'>')