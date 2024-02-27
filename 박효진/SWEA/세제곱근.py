T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if round(N ** (1/3)) ** 3 == N:
        num = round(N**(1/3))
    else:
        num = -1
    print(f'#{tc}', num)