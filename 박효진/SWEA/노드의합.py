T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    level = [0] * (N + 2)
    for _ in range(M):
        leaf, value = map(int(input).split())
        level[leaf] = value
        
    
