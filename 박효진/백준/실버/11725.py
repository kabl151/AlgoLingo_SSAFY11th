# def dfs(node):
#     global new_lst
#     if node:
#         for i in lst[node]:
#             if judge[i] == False:
#                 judge[i] = True
#                 new_lst[i].append(node)
#                 dfs(i)
import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]

for i in range(N-1):
    par, child = map(int,input().split())
    lst[child].append(par)
    lst[par].append(child)

new_lst = [[] for _ in range(N+1)]
stack = []
judge = [False]*(N+1)
judge[1] = True
for i in lst[1]:
    if judge[i] == False:
        new_lst[i].append(1)
        judge[i] = True
# dfs(1)

print(lst)
print(new_lst)

