import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
pang = list(map(int, input().split()))
pang_lst = []
result = []
for i in range(1, len(pang) + 1):
    pang_lst += [[i,pang[i-1]]]
dq = deque(pang_lst)

for j in range(len(pang_lst)):
    result.append(dq[0][0])
    rotate_num = dq.popleft()
    if rotate_num[1] > 0:
        dq.rotate(-((rotate_num[1])-1))
    else:
        dq.rotate(-rotate_num[1])

print(*result)

