import sys
input = sys.stdin.readline

N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))

lst = set(arr_N) & set(arr_M) 

arr = [0]* 500001

for i in range(M):
    if arr_M[i] in lst:
        arr[i] = 1
result = arr[:M:]
print(*result)