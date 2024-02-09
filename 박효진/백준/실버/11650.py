N = int(input())
lst = []
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr)
for i in range(N):
    result = arr[i]
    print(*result)