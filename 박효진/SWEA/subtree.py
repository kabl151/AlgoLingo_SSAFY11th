'''
1
5 1
2 1 2 5 1 6 5 3 6 4
'''
def tree(N):
    if len(node[N]) != 0:
        for i in node[N]:
            subtree.append(i)
            tree(i)

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    line = list(map(int, input().split()))
    max_num = max(line)
    node = [[] for _ in range(max_num + 1)]
    
    for i in range(0, E * 2,2):
        node[line[i]].append(line[i+1])
    
    subtree = []
    subtree.append(N)
    
    tree(N)

    print(f'#{tc}', len(subtree))