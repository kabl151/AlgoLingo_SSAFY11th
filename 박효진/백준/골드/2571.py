arr = [[0] * 101 for _ in range(101)]
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
print(arr)
    # for i in range(1,101):
    #     for j in range(1,101):
    #         if arr[i][j] == 1: