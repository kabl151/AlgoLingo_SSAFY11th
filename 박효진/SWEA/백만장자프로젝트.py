# 제일큰거 찾고, 왼쪽 데이터 더하기.

# sort > 최댓값 찾아. 왼쪽다더해.
# 그다음 최댓값 찾아. 오른쪽에 앞에있던 최댓값 나오면 pass

# 반복...
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     money = 0
#     while len(arr) != 0:
#         max_num = max(arr)
#         max_num_idx = arr.index(max_num)
#         for j in range(max_num_idx):
#             money += max_num - arr[j]
#         for k in range(max_num_idx+1):
#             arr.pop(0)

#     print(f'#{tc} {money}')


# ----------------------------------------------
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     money = 0
#     while len(arr) != 0:
#         max_num = max(arr)
#         max_num_idx = arr.index(max_num)
#         for j in range(max_num_idx):
#             money += max_num - arr[j]
#         arr = arr[max_num_idx+1::]
#     print(f'#{tc} {money}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    money = 0
    while len(arr) != 0:
        max_num = max(arr)
        max_num_idx = arr.index(max_num)
        max_num*len(arr[:max_num_idx])-sum(arr[:max_num_idx])
        for j in range(max_num_idx):
            money += max_num - arr[j]
        arr = arr[max_num_idx+1::]
    print(f'#{tc} {money}')


T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    price = list(map(int,input().split()))

    max_price = price[-1]
    margin = 0

    for p in price[::-1]:
        if p > max_price:
            max_price = p
        else:
            margin += max_price - p

    print(f'#{test_case} {margin}')    