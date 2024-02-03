# 리스트 갯수 N과 연속적인 날자 수 K 할당
# N, K = map(int, input().split())

# 두번째 input 값을 공백을 기준으로나눈 list 할당
# tem_lst = list(map(int, input().split()))

# 1. 새로운 리스트를 만들어서 수열 값을 할당하는데
# lst[0] + lst[1] + ... lst[n] 까지 구한 후
# lst[0] + lst[1] + ... lst[n-k+1] 까지 구한 값을 빼는 방식

# # 2. 새로운 리스트를 만들어서 수열 값을 할당을 더한다 (시간초과)
# lst[0] + lst[1] + ... lst[k] 까지 합을 할당
# for i in range(0, N - K + 1):
#     tem_sum = 0
#     for j in range(i, i + K):
#         tem_sum += tem_lst[j]
#     new_lst += [tem_sum]
# print(max(new_lst))

#lst[0] + lst[1] + ... lst[k] 까지 합을 할당
# for i in range(0, N-K+1):
#     tem_sum = 0
#     for j in range(i, i + K):
#         tem_sum += tem_lst[j]
#     new_lst += [tem_sum]

# print(max(new_lst))


# max_sum = 0       (시간초과)
# for i in range(0, N-K+1):
#     sum_num = 0
#     for j in range(i, i + K):
#         sum_num += tem_lst[j]
#     if max_sum <= sum_num:
#         max_sum = sum_num

# print(max_sum)



# max_sum = -100 * K    (시간초과)
# for i in range(0, N-K+1):
#     sum_num = 0
#     for j in range(i, i + K):
#         sum_num += tem_lst[j]
#     if sum_num >= max_sum:
#         max_sum = sum_num
#     else:
#         pass

# print(max_sum)

# max_sum = -100 * K    (시간초과)
# for i in range(0, N-K+1):
#     sum_num = 0
#     for j in range(i, i + K):
#         sum_num += tem_lst[j]
#     if sum_num >= max_sum:
#         max_sum = sum_num

# 리스트 갯수 N과 연속적인 날자 수 K 할당
N, K = map(int, input().split())

# 두번째 input 값을 공백을 기준으로나눈 list 할당
tem_lst = list(map(int, input().split()))

first_num = 0
for i in range(0, K):
    first_num += tem_lst[i]
max_num = first_num
for j in range(K, N):
    first_num = first_num + tem_lst[j] - tem_lst[j - K]
    if max_num <= first_num:
        max_num = first_num

print(max_num)