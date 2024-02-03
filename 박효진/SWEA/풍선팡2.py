T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if max_num <= arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i][j-1] + arr[i-1][j]:
                max_num = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i][j-1] + arr[i-1][j]

    print(f'#{test_case} {max_num}')
    # ///////////////////////////////////////////////////////////////////////////////////
