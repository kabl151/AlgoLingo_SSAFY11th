# 리스트 갯수 N과 연속적인 날자 수 K 할당
N, K = map(int, input().split())

# 두번째 input 값을 공백을 기준으로나눈 list 할당
tem_lst = list(map(int, input().split()))
#-------------------------------------------------------------------------------
# 1. 새로운 리스트를 만들어서 수열 값을 할당하는데
# lst[0] + lst[1] + ... lst[n] 까지 구한 후
# lst[0] + lst[1] + ... lst[n-k+1] 까지 구한 값을 빼는 방식
#-------------------------------------------------------------------------------
# 2-1 lst[0] + lst[1] + ... lst[k] 까지 합을 할당
# 새로운 리스트를 만들어서 수열 값을 할당을 더한다 (시간초과)
for i in range(0, N - K + 1):
    tem_sum = 0
    for j in range(i, i + K):
        tem_sum += tem_lst[j]
    new_lst += [tem_sum]
print(max(new_lst))

# 2-2 리스트에 할당하지 않고 for문의 sum_num과 max_sum을 바로 비교 후 출력 (시간초과)
max_sum = 0       
for i in range(0, N-K+1):
    sum_num = 0
    for j in range(i, i + K):
        sum_num += tem_lst[j]
    if max_sum <= sum_num:
        max_sum = sum_num
print(max_sum)

# 2-3 2중 for 문을 사용하지 않고, 임시로 max_num을 할당한 후, 
# 리스트 데이터의 오른쪽 데이터를 더하고 왼쪽 데이터를 빼서 비교하는 방식으로 진행

first_num = 0   # 데이터를 비교하기 위한 첫 K까지의 합을 할당하기 위한 초기 설정
for i in range(K):              #index기준으로 0부터 K-1 까지 계산.
    first_num += tem_lst[i]     #i가 k-1까지 돈 list의 데이터들을 다 first_num에 더해준다.
max_num = first_num             #비교를 위해 첫 K개의 데이터 합을 max_num으로 설정해준다.
for j in range(K, N):           #index기준으로 K부터 리스트의 > 방향으로 한칸씩 밀어 N-1 까지 비교한다.
    first_num = first_num + tem_lst[j] - tem_lst[j - K] # tem_lst[j] : 오른쪽 데이터, tem_lst[j-K] : 왼쪽데이터
    if max_num <= first_num:    # 비교 후 큰 값 재할당
        max_num = first_num

print(max_num)                  #출력
