import sys
input = sys.stdin.readline

N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))

arr = [0]* M

for i in arr_N:
    for j in range(M):
        if i == arr_M[j]:
            arr[j] += 1
result = arr[:M:]
print(*result)