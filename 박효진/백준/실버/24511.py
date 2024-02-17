# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# M = int(input())
# C = list(map(int, input().split()))

# queuestack = []
# result = []

# for i in range(N):
#     queuestack.append([A[i],B[i]])
# for j in C:
#     for k in range(N):
#         if queuestack[k][0] == 0:
#             queuestack[k][1], j = j, queuestack[k][1]
#         else:
#             pass
#     result.append(j)
# print(*result)



# ============================================
from collections import deque

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queuestack = []
result = []

for i in range(N):
    if A[i] == 0:
        queuestack.append(B[i])
dq = deque(queuestack)
for i in C:
    dq.appendleft(i)
    result.append(dq.pop())
print(*result)