
def build_graph(input_data):                        # graph 데이터 가공
    graph = {}                                      # 빈 딕셔너리 선언
    pairs = input_data.split()                      # input_data에 따라 달라짐, 문자열로 진행
    for i in range(0, len(pairs), 2):               # 짝수번째 데이터만 가져오고 인덱스를 통해 데이터를 나눈다
        node = pairs[i]                             # 노드 정의
        neighbors = [pairs[i+1]]                    # 노드와 연결된 이웃
        if node not in graph:                       # 새로 노드가 정의 됐다면 데이터 추가
            graph[node] = []                        # 빈 리스트로 넣으며
        graph[node].extend(neighbors)               # 데이터가 추가되면 {'a' : [b, c]} 의 형태를 띈다
    return graph                                    # 가공된 graph 데이터를 return한다.

def dfs(graph, start_node, end_node, path = None):  # DFS 함수 정의 path = None은 길을 못찾았다는 의미(재귀 위함)
    if path is None:                                # 길 탐색을 위한 path list 초기화
        path = []
    path = path + [start_node]                      # 가장 처음 노드를 리스트에 추가해준다
    if start_node == end_node:                      # 재귀하면서 start_node가 바뀌는데, end_node와 같아진다면
        return path                                 # return path를 통해 경로 자체를 가져온다
    if start_node not in graph:                     # 막다른 길을 만나면
        return False                                # None을 반환하여 되돌아가게 한다
    for node in graph[start_node]:                  # dict 데이터에서 연결된 neighbors 탐색
        if node not in path:                        # path에 없다면 (중복되지 않았다면) 다음 노드에서 새로운 길 탐색을 위한 재귀
            new_path = dfs(graph, node, end_node, path) # 이부분 이해가 어려움... ㅠㅠ
            if new_path:
                return new_path
    return None

input_data = '0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7'  # 들어올 그래프 데이터
start_node = '0'                                    # 시작 노드
end_node = '99'                                     # 종료 노드
graph = build_graph(input_data)                     # 그래프 (dict 표현)
path = dfs(graph, start_node, end_node)             # 경로 탐색
print(path)                                         # ['0', '1', '4', '3', '7', '99']
