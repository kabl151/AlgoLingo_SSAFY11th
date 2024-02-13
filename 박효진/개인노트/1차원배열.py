# # 1차원 배열의 선언
# arr_1 = list()
# arr_2 = []
# arr_3 = [2024, 1, 31]
# arr_4 = [0]* 10

# print(arr_1) # []
# print(arr_2) # []
# print(arr_3) # [2024, 1, 31]
# print(arr_4) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# # 1차원 배열의 접근 예시
# arr = [19, 's', '79', 132]
# print(arr[1])   # s
# arr[1] = 132    # arr 리스트의 1번 인덱스 접근
# print(arr[2])   # 79
# arr[2] = 1004   # arr 리스트의 2번 인덱스 접근
# print(arr) # [19, 132, 1004, 132]

# # BubbleSort
# lst = [13, 2, 6, 15, 3, 10]
# N = len(lst)                    
# for i in range(N - 1, 0, -1):   # 탐색 횟수가 정렬될수록 줄어들기 때문에 (5,4,...,1)
#     for j in range(0, i):       # 정렬되기 전 탐색 횟수는 많고, i가 돌수록 줄어든다
#         if lst[j] > lst[j+1]:   # 만약 왼쪽 데이터가 오른쪽 데이터보다 크다면 교환한다
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(lst) # [2, 3, 6, 10, 13, 15]

# Counting Sort
data_lst = [1, 2, 0, 2, 3, 2, 4, 4, 1]
data_counts = []
temp = []

data_counts = [0] * (4 + 1)
# 각 데이터 위치별 카운트횟수 증가
for i in range(0, len(data_lst)):
    data_counts[data_lst[i]] += 1
# 누적합 구하기
for i in range(1, 4 + 1):
    data_counts[i] += data_counts[i-1]

# 리스트 우측 데이터부터 누적합을 통해 흩뿌리기
for i in range(5-1, -1, -1):
    data_counts[data_lst[i]] -= 1
    temp[data_counts[data_lst[i]]] = data_lst[i]

print(temp)