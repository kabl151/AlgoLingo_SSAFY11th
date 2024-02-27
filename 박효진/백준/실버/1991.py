import sys
input = sys.stdin.readline
#전위
def pre_order(node):
    global result
    if node:
        result.append(par[node])
        pre_order(left[node])        
        pre_order(right[node])        
#중위
def in_order(node):
    global result
    if node:
        in_order(left[node])        
        result.append(par[node])
        in_order(right[node])        
        
#후위
def post_order(node):
    global result
    if node:
        post_order(left[node])        
        post_order(right[node])        
        result.append(par[node])

table = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
left = [0]*(N+1)
right = [0]*(N+1)
par = [0]*(N+1)

result = []
for i in range(N):
    order = list(map(str, input().split()))
    par[table.index(order[0])] = table.index(order[0])
    if order[1] != '.':
        left[table.index(order[0])] = table.index(order[1])
    if order[2] != '.':
        right[table.index(order[0])] = table.index(order[2])
pre_order(1)
in_order(1)
post_order(1)

wd = ''
for i in result:
    wd += table[i]
print(wd[:N])
print(wd[N:2*N])
print(wd[2*N:3*N])