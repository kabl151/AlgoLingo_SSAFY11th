# import sys
# sys.stdin = open('input.txt', 'r')
# 후위 탐색
def post_order(node):
    global result
    if node:
        post_order(left[node])
        post_order(right[node])
        if par[node] == '+':
            result.append(par[left[node]] + par[right[node]])
            par[node] = par[left[node]] + par[right[node]]
        elif par[node] == '-':
            result.append(par[left[node]] - par[right[node]])
            par[node] = par[left[node]] - par[right[node]]
        elif par[node] == '*':
            result.append(par[left[node]] * par[right[node]])
            par[node] = par[left[node]] * par[right[node]]
        elif par[node] == '/':
            result.append(par[left[node]] / par[right[node]])
            par[node] = par[left[node]] / par[right[node]]

T = 10
for tc in range(1, T + 1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    result = []
    for _ in range(N):
        info = list(map(str, input().split()))
        if len(info) == 4:
            node = int(info[0])
            oper = info[1]
            left_node = int(info[2])
            right_node = int(info[3])
            par[node] = oper
            left[node] = left_node
            right[node] = right_node
        elif len(info) == 2:
            node = int(info[0])
            num = int(info[1])
            par[node] = int(num)
    post_order(1)
    print(f'#{tc}', int(result[-1]))