import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [x for x in range(1,N+1)]
result_arr = arr
for _ in range(M):
    i, j = map(int, input().split())
    reversed_part = result_arr[i-1:j][::-1]
    result_arr = result_arr[:i-1] + reversed_part + result_arr[j:]

print(*result_arr)
