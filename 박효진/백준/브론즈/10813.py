import sys
input = sys.stdin.readline


N, M = map(int, input().split())
bk = [x for x in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    bk[i-1], bk[j-1] = bk[j-1], bk[i-1]

print(*bk)