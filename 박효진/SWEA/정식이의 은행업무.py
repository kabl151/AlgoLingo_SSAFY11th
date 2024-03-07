T = int(input())
for tc in range(1, T+1):
    second = list(map(int, input().rstrip()))
    third = list(map(int, input().rstrip()))
    second_lst = []
    third_lst = []
    for i in range(len(second)):
        if second[i] == 1:
            second[i] = 0
            second_num = ''
            for j in range(len(second)):
                second_num += (str(second[j]))
            second_lst.append(int(second_num,2))
            second[i] = 1
        elif second[i] == 0:
            second[i] = 1
            second_num = ''
            for j in range(len(second)):
                second_num += (str(second[j]))
            second_lst.append(int(second_num,2))
            second[i] =0
    for i in range(len(third)):
        if third[i] == 0:
            third[i] = 1
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num,3))
            third[i] = 2
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num, 3))
            third[i] = 0

        elif third[i] == 1:
            third[i] = 2
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num, 3))
            third[i] = 0
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num, 3))
            third[i] = 1

        elif third[i] == 2:
            third[i] = 0
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num, 3))

            third[i] = 1
            third_num = ''
            for j in range(len(third)):
                third_num += (str(third[j]))
            third_lst.append(int(third_num, 3))

            third[i] = 2
    print(f'#{tc}', *set(second_lst) & set(third_lst))