def omok(i,j):
    for k in range(8):
        stack =[]
        stack.append([i,j])
        for l in range(4):
            if i+di[k]*l >= 0 and i+di[k]*l < N and j+dj[k]*l >= 0 and j+dj[k]*l < N and arr[i+di[k]*l][j+dj[k]*l] == 'O':
                stack.append([i+di[k]*l][j+dj[k]*l])
            else:
                continue
        if len(stack) == 5:
            result = 'YES'
            return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    stack = []
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                omok(i,j)
    print(result)