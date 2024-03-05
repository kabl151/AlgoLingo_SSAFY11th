T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    new_lst = []
    tem_lst = list(map(int, input().split()))
    for i in range(0, N - M + 1):
        tem_sum = 0
        for j in range(i, i + M):
            tem_sum += tem_lst[j]
        new_lst += [tem_sum]
    max_num = max(new_lst)
    min_num = min(new_lst)
    print(f'#{test_case} {max_num - min_num}')

