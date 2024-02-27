'''
3
5 1
2 1 2 5 1 6 5 3 6 4
'''
def tree(N):
    if len(lst[N]) != 0:
        for i in range(len(lst[N])):
            subtree.append(lst[N][i])
            tree(lst[N][i])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    lines = list(map(int,input().split()))
    mx_node_num = max(lines)
    # 인덱스 번호를 받을 빈 요소(맨 앞은 더미데이터)
    lst = [[] for _ in range(mx_node_num+1)]
    for i in range(0, len(lines), 2):
        lst[lines[i]].append(lines[i+1])
    subtree = []
    subtree.append(N)
    tree(N)
    print(f'#{tc}',len(subtree))