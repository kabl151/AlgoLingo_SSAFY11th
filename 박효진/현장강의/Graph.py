# 그래프
# -> 데이터들끼리 다대다 관계를 가지게 되는 자료구조
#               N : M

# 인접 리스트 : 정점 i가 인접한(연결 관계를 가진)
#              노드 정보를 리스트로 저장...
# 정점의 갯수 V 와 간선의 갯수 E
V, E = map(int, input().split())  # 5 8
adj = [[] for _ in range(V + 1)]  # 노드 갯수 N 만큼, 비어있는 리스트를 준비.# ..!

# 반복문을 통해서 간선의 정보를 각각 입력 받습니다...!
# 각 줄에 시작점과 종료점을 입력..
for _ in range(E):  # 간선의 갯수 만큼 순회...
    # 해당 줄에 시작점 종료점 정보를 입력
    start, end = map(int, input().split())  # '1 2' 1 <-> 2
    # 시작정점과 끝정점을 서로 연결한다... v -> w
    adj[start].append(end)  # start -> end
    adj[end].append(start)  # end -> start

# DFS 탐색.. 시작정점 i 가 주어진다면?? (재귀함수)
def dfs(i):
    # 현재 노드를 방문체크! (출력)
    visited[i] = True
    print('-', i, end='')

    # 현재 i 정점으로 부터 인접한 노드를 계속해서 방문...! (탐색)
    for w in adj[i]:  # 인접한 노드들을 순회...
        # 아직 방문하지 않았던 노드만 방문...
        if visited[w] == False:
            dfs(w)


# 방문체크를 하기 위한 visited 배열
visited = [False] * (V + 1)
dfs(1)  # 1번 정점을 시작으로 해서 나머지 정점으로 모두 탐색...!