T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()
    ans_str = []
    ans_int = []
    for i in range(N//4):
        ans_str.append(num[:N//4:])
        ans_str.append(num[N//4:N//2:])
        ans_str.append(num[N//2:3*N//4:])
        ans_str.append(num[3*N//4::])
        num = num[-1] + num[:-1:]
    for i in ans_str:
        ans_int.append(int(i, 16))
    ans_int = list(set(ans_int))
    ans_int.sort()
    ans_int.reverse()
    print(f'#{tc}', ans_int[K-1])