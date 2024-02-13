T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    arr[N//2][N//2] = arr[N//2 + 1][N//2 + 1] = 2   #백
    arr[N//2][N//2 +1] = arr[N//2 + 1][N//2] = 1   #흑

    for turn in range(M):
        x, y, info = map(int, input().split())
        di = [0, 1, 1, 1, 0, -1, -1, -1]
        dj = [1, 1, 0, -1, -1, -1, 0, 1]
        stack = []
        num = 1
        arr[x][y] = info
        for i in range(1, N-1):
            for j in range(1, N-1):
                for k in range(8):
                    if arr[i+di[k]][i+dj[k]] == info or arr[i+di[k]][i+dj[k]] == 0:
                        continue
                    else:
                        while True:
                            if arr[i+num*di[k]][i+num*dj[k]] != info and arr[i+di[k]][i+dj[k]] != 0:
                                arr[i+di[k]][i+dj[k]].append(stack)
                                num += 1
                            elif arr[i+num*di[k]][i+num*dj[k]] == info:

                    # elif arr[i+di[k]][i+dj[k]] == info or arr[i+di[k]][i+dj[k]] == 0:
                    #     pass

            # if arr[x][y+1] != info:
                
            # if arr[x+1][y+1] != info:

            # if arr[x+1][y] != info:

            # if arr[x+1][y-1] != info:

            # if arr[x][y-1] != info:

            # if arr[x-1][y-1] != info:

            # if arr[x-1][y] != info:

            # if arr[x-1][y+1] != info:


    # 흑 - 백 순서로 하고, 입력은 주어지기 때문에
    # 놓을 수 없는 곳은 굳이 고려안해도됨

print(arr)