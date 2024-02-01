T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(5)]
    max_lst = []
    sum_num = 0
    sum_num_dia = 0
    sum_num_dia2 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                sum_num_dia += arr[i][j]
    max_lst.append(sum_num_dia)

    for i in range(5):
        for j in range(5):
            if i + j == 4:
                sum_num_dia2 += arr[i][j]
    max_lst.append(sum_num_dia2)

    for i in range(5):
        sum_num = sum(arr[i])
        max_lst += [sum_num]

    for i in range(5):
        for j in range(5):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for j in range(5):
        sum_num = sum(arr[j])
        max_lst += [sum_num]

    print(max_lst)
    print(f'#{tc} {max(max_lst)}')