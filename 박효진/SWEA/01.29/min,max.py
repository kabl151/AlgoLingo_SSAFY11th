T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))
    min_lst = min(lst)
    max_lst = max(lst)
    print(f'#{test_case} {max_lst - min_lst}')