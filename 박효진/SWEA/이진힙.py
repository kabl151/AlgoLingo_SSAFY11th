T = int(input())
for tc in range(1,T+1):
    # 추가하는 enqueue
    def enqueue(heap, item):
        heap.append(item)
        idx = len(heap) - 1
        while idx != 1:
            parent = idx // 2
            if heap[parent] > heap[idx]:
                heap[parent], heap[idx] = heap[idx], heap[parent]
                idx = parent
            else:
                break
    # 최소힙
    heap = [None]
    N = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        enqueue(heap,i)
    c = N
    total_num = 0
    while c != 1:
        c //= 2
        total_num += heap[c]
    print(f'#{tc}',total_num)