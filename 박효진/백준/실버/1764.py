import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set_N = set(input().rstrip() for _ in range(N))
set_M = set(input().rstrip() for _ in range(M))

result = list(set_N & set_M)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])