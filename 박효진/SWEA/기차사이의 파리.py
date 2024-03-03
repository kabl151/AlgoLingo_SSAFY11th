T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(float, input().split())
    print(f'#{tc}', D / (A + B) * F)