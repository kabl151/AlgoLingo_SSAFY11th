T = int(input())
for tc in range(1, T + 1):
    
    # 완전이진트리 / LVR 규칙

    # 완전 이진 트리의 작성 방법 사용
    def complete_binary_tree(N, left, right, par):
        for i in range(1, N // 2 + 1):  # 루트 1번부터 N번 노드까지 만들기 위한 반복문
            if i * 2 <= N:  # 왼쪽 자식을 넣기 위한 조건
                left[i] = i * 2  # 왼쪽 자식 탐색
                par[i * 2] = i  # 자식 인덱스를 통해 부모에도 등록
            if i * 2 + 1 <= N:  # 오른쪽 자식 탐색
                right[i] = i * 2 + 1
                par[i * 2 + 1] = i
        return


    # 중위 탐색 알고리즘 (LVR)
    def in_order(node):
        global cnt
        if node:
            in_order(left[node])
            cnt += 1
            arr[cnt] = node
            in_order(right[node])


    N = int(input())

    # 트리를 만들어보자
    # 왼쪽 자식 / 오른쪽 자식 / 부모 인덱스 생성
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)

    complete_binary_tree(N, left, right, par)

    # 중위 탐색(방문순서를 입력하는 데이터를 찾아야 한다)
    arr = [0]*(N + 1)
    cnt = 0
    in_order(1)  # 완전 이진 트리에서는 루트가 무조건 1이므로

    c = N
    while par[c]!=0:    # 부모가 있으면
        c = par[c]      # 부모를 새로운 자식으로 두고
    root = c            # 더이상 부모가 없으면 root

    print(f'#{tc}', arr.index(root), arr.index(N//2))  # 인덱스에 저장된 값이 중위 탐색 순서