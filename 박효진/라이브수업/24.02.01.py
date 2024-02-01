# 검색(= 탐색 Search)

# 탐색의 종류
# - 순차 탐색(sequential search)
# - 이진 탐색(binary search)
# - 해쉬

# 순차 탐색(sequential search)
# 정렬이 되어있지 않은 경우
def sequentialSearch(arr, n, key):
    i = 0
    while i < n and arr[i] != key:
        i = i + 1
    if i< n : return i
    else : return -1
# for 문을 사용하여 구현
def sequentialSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    else:
        return -1
# 정렬이 되어있지 않은 경우
def sequentialSearch2(arr, n, key):
    i = 0
    while i < n and arr[i] != key:
        i = i + 1
    

# 이진 검색 알고리즘 형태(그대로 이용 가능) (***기본 조건 : 정렬상태***)
def BinarySearch(arr, N, key):
    start = 0 # 구간초기화 (=lft)
    end = N-1 # 구간초기화 (rght)
    while start <= end: # 검색 구간이 유효하면 반복(범위)
        middle = (start + end)//2 # 중앙 원소 인덱스
        if arr[middle] == key: # 검색성공
            return middle
        elif arr[middle] > key: # 중앙값이 key보다 크면
            end = middle - 1 # -1, +1 을 넣어주는 이유는 middle값 그대로 사용한다면 while문의 무한반복에 빠지게된다(반례 : start 0, end 1)
        else:
            start = middle + 1 # 중앙값이 key보다 작으면
    return -1    # 검색실패 (범위 이탈)

# 선택 정렬
def SelectionSort(arr, N):
    for i in range(N-1):    # i 주어진 구간의 시작
        min_idx = i     # 맨 앞 원소를 최솟값 위치로 가정
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




# 셀렉션 알고리즘
# 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고 배열의 k번째를 반환한다.
def Select(arr, k):
    for i in range(0, k):
        min_index = i
        for j in range (i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k - 1]

def selection_sort(arr, N):
    for i in range(N-1):    # 구간이 시작 i, 2개의 원소가 남을 때까지
        min_idx = i         # 구간의 최솟값 위치 min_idx, 첫 원소를 최소로 가정
        for j in range(i+1, N): # 실제 최솟값을 찾을 위치 j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx] # 최솟값을 구간의 맨 앞으로 이동
    return

# 버블정렬
def bubble_sort(arr, N): # 바로 옆에 있는 요소와 비교해서 교환
    for i in range(N - 1, 0, -1): # 요소의 끝까지 반복시행하며 오른쪽에서 왼쪽으로 진행
        for j in range(i):
            #바로 옆에있는 값과 비교한다
            #이 때에 오름차순에 어긋나면 교체한다
            #           -> 오른쪽 값이 더 작다면 교체하겠다
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]