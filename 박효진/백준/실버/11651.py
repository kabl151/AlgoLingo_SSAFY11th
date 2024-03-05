N = int(input())
lst = []
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    arr[i] = arr[i][::-1]
arr = sorted(arr)
for i in range(N):
    arr[i] = arr[i][::-1]
for i in range(N):
    result = arr[i]
    print(*result)