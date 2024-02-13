import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dct = {}
for i in range(1, N+1):
    name = input().rstrip()
    dct[name] = str(i)
    dct[str(i)] = name

for i in range(M):
    problem = input().rstrip()
    print(dct[problem])