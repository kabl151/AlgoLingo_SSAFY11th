import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip())
lst = []
result = []
# 우선순위 : 카운트, 길이, 사전순
for i in range(N):
    wd = input().rstrip()
    lst.append(wd)
    
set()