# 부분 수열의 합
def permutation(n,sum_num):
    global cnt
    if sum_num == K and n == N:
        cnt += 1
        return

    for i in range(N):
        if sum_num < K:
            path.append(arr[i])
            permutation(i,sum_num + arr[i])
            path.pop()
        elif sum_num > K:
            return

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    path = []
    permutation(0,0)
    print(f'#{tc}', cnt)