def in_order(node):
    global result
    if node:
        in_order(left[node])
        result += par[node]
        in_order(right[node])
T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    result = ''
  
    for _ in range(N):
        info = list(map(str, input().split()))
        if len(info) == 4:
            par[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
        elif len(info) == 3:
            par[int(info[0])] = info[1]
            left[int(info[0])] = int(info[2])
        elif len(info) == 2:
            par[int(info[0])] = info[1]
    in_order(1)
    print(f'#{tc}', result)