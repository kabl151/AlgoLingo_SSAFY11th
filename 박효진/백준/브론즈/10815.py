import sys
input = sys.stdin.readline

N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))
result = []
for i in arr_M:
    if i in arr_N:
        result.append(1)
    else:
        result.append(0)
print(*result)