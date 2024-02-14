
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr_N = list(map(int, input().split()))

# M = int(input())
# arr_M = list(map(int, input().split()))

# arr = [0]* M

# for i in arr_N:
#     for j in range(M):
#         if i == arr_M[j]:
#             arr[j] += 1
# result = arr[:M:]
# print(*result)

# ---------------------------------------------

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr_N = list(map(int, input().split()))

# M = int(input())
# arr_M = list(map(int, input().split()))

# arr = [0] * 500000
# for i in arr_N:
#     if i in arr_M:
#         arr[arr_M.index(i)] += 1
# print(*arr[:M:])

# ---------------------------------------------
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr_N = list(map(int, input().split()))

# M = int(input())
# arr_M = list(map(int, input().split()))

# for i in arr_M:
#     print((arr_N.count(i)), end = ' ')

# ------------------------------------------------

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr_N = list(input().split())

# M = int(input())
# arr_M = list(input().split())

# for i in arr_M:
#     print((arr_N.count(i)), end = ' ')

# ------------------------------------------------

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr_N = list(input().split())
# dct = {}
# M = int(input())
# arr_M = list(input().split())
# for i in range(M):
#     dct[arr_M[i]] = 0
# for j in arr_N:
#     if j in arr_M:
#         dct[j] += 1
# for k in arr_M:
#     print(dct[k], end = ' ')

# ----------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))

arr = [0] * 20000001

for idx in arr_N:
    arr[idx] += 1
for idx in arr_M:
    print(arr[idx], end =' ')

