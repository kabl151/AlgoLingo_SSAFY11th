import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().rstrip().split())
dq = deque([x for x in range(1, N+1)])
result = []
while dq:
    dq.rotate(-(K-1))
    result.append(dq.popleft())
print('<', end = '')
print(*result, end = '', sep =', ')
print('>')