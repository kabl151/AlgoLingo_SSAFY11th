import sys
input = sys.stdin.readline

N = int(input())
arr_N = set(map(int, input().split()))
M = int(input())
arr_M = list(map(int, input().split()))

arr_N = sorted(list(arr_N))
arr_M.sort

for i in arr_M:
    if i in arr_N:
        print(1)
    else:
        print(0)