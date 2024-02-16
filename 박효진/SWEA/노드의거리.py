def bfs(graph,S,V):
    queue = []
    visited = [-1] * (V + 1)
    queue.append(S)
    visited[S] = 0
    while queue:
        t = queue.pop(0)
        if t == G:
            return visited[t]
        for i in graph[t]:
            if visited[i] == -1:
                queue.append(i) 
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{tc}', bfs(graph,S,V))