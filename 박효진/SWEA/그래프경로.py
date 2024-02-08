T= int(input())
for tc in range(1, T+1):
    def dfs(i):
        visited[i] = True
        print('-',i,end='')
        for w in adj[i]:
            if visited[w] == False:
                dfs(w)
                
    V, E = map(int, input().split())
    adj = [[]for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    visited = [False] * [V + 1]
    # test_node = list(map(int, input().split()))
    dfs(1)
    