T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if N**2 >= i**2 + j**2:
                result.append([i,j])
    print(f'#{tc}',len(result))