T = int(input())
for tc in range(1, T + 1):
    # 완전 이진 트리
    def complete_tree(N, left, right, par):
        for i in range(1, N // 2 + 1):
            if 2 * i <= N:
                left[i] = 2 * i
                par[2 * i] = i
            if 2 * i + 1 <= N:
                right[i] = 2 * i + 1
                par[2 * i + 1] = i
    # post_order
    def post_order(node):
        global total_sum
        if node:
            post_order(left[node])
            post_order(right[node])
            if left[node]:
                result[node] += result[left[node]]
            if right[node]:
                result[node] += result[right[node]]

    N, M, L = map(int, input().split())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)

    complete_tree(N, left, right, par)
    result = [0] * (N + 1)
    for _ in range(M):
        leaf_node, num = map(int, input().split())
        result[leaf_node] = num

    post_order(1)

    
    print(f'#{tc}',result[L])