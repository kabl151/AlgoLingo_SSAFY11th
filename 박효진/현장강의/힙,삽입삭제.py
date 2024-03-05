# 최소힙 : 부모가 자식보다 항상 작은 값을 유지하는 완전 이진 트리
# 일차원 배열로서 작업...
# 삽입 : enqueue
# 삭제 : dequeue


# 삽입하는 연산 enqueue
# 완전 이진 트리를 유지하기 위해 추가되는 단말 노드 하나 삽입
# 단말노드를 기준으로 부모와 자리 바꾸기를 진행...!
# while 더 바꿀 필요가 없을 때 까지... = 부모가 자식보다 작은값(최소힙)이거나 부모가 없는 상황일때까지
def enqueue(hq, item):
    hq.append(item)     # 단말 노드 item을 추가하고
    current = len(hq) - 1   # 추가한 요소의 인덱스
    while current != 1:     # 현재의 이 노드가 루트노드까지 진행했을 때까지 진행하고 종료하겠다
        parent = current // 2       # 부모의 인덱스 값 (몫나누기 //2 하면 부모)
        if hq[parent] > hq[current]:    # 부모의 요소보다 자식이 작은 경우 = 자리바꾸기
            hq[parent], hq[current] = hq[current], hq[parent]
            current = parent        # 인덱스가 변경되었으므로 내 자신의 인덱스를 갱신
        else:
            break       # 부모의 요소보다 자식이 클때는 자리를 바꾸지 않고 종료

# 삭제하는 연산 dequeue
# 힙의 삭제과정은 루트 노드를 삭제하고 가장 끝에있는 단말 노드 하나를 루트노드로 끌고온다
# 왼쪽 자식과 오른쪽 자식 중에서 나보다 더 작은값(최소힙)이 있다면 있다면 그 값과 자리바꾸기 진행
def dequeue(hq):
    # 임시저장
    data = hq[1]
    if len(heap) == 2:  # 데이터가 하나만 있을때
        return hq.pop()
    elif len(heap) == 1:# 데이터가 비어 있을때
        return -1
    # 루트 노드 위치에 가장 끝에 있는 단말 노드를 재배치
    hq[1] = hq.pop()
    current = 1
    N = len(heap)
    # 힙 자료구조가 유지되게끔 자리바꿈을 계속 진행
    # 루트 노드로부터 왼쪽 자식과 오른쪽 자식 중에서 나보다 더 작은 값이 있다면 교체
    # 해당 값이 단말 노드까지 가게되면 정지!
    while current < N:
        # 왼쪽/ 오른쪽 자식 인덱스
        left_child, right_child = current * 2, current *2 +1
        # 2가지 경우가 있음
        # 1. 왼쪽과 오른쪽 자식이 모두 있는 경우
        if left_child < N and right_child < N:
            if hq[left_child] < hq[current] or hq[right_child] < hq[current]:
                # 자리교체를 수행해줘야 하는 경우
                # 왼쪽 자식과 오른쪽 자식 중에서 더 작은 것과 자리 교체를 수행
                if hq[left_child] < hq[current]:
                    hq[left_child], hq[current] = hq[current], hq[left_child]
                    # 자리교체 했으니 인덱스도 교환 및 갱신
                    current = left_child
                else:
                    hq[right_child], hq[current] = hq[current], hq[right_child]
                    current = right_child
            else:
                break
        # 2. 왼쪽 자식만 있는 경우(완전 이진 트리이기때문에 오른쪽 자식만 있는 경우 x)
        elif left_child < N and right_child >= N:
            # 왼쪽 자식과 오른쪽 자식 중에서 더 작은 것과 자리 교체를 수행
            if hq[left_child] < hq[current]:
                hq[left_child], hq[current] = hq[current], hq[left_child]
                # 자리교체 했으니 인덱스도 교환 및 갱신
                current = left_child
            else:
                break
        else:
            break
    return data

heap = [None]

enqueue(heap, 30)
enqueue(heap, 50)
enqueue(heap, 20)
enqueue(heap, 10)
enqueue(heap, 80)

for i in range(5):
    item = dequeue(heap)
    print(item)