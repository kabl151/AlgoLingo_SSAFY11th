T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*10001
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi):
            arr[i] += 1
    print(arr[:10:])