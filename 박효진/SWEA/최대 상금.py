T = int(input())
for tc in range(1, T + 1):

    def permutation(n):
        global times
        if n == len(result):
            cnt = 0
            for i in range(len(path)):
                if path[i] != result[i]:
                    cnt += 1
            if n == 6 and cnt == 4:
                cnt_lst.append((cnt + 2) // 2)
            else:
                cnt_lst.append((cnt + 1) // 2)
            final.append(path[:])
            return
        for i in range(len(result)):
            if used[i] == False:
                used[i] = True
                path.append(result[i])
                permutation(n + 1)
                path.pop()
                used[i] = False


    arr, times = map(int, input().split())
    result = []
    path = []
    lst = []
    cnt = 0
    final = []
    cnt_lst = []
    while arr != 0:
        result.append(arr % 10)
        arr = arr // 10
    result.reverse()
    used = [False] * (len(result))
    permutation(0)

    final_lst = []
    if max(cnt_lst) < times:
        if len(set(result)) == len(result):
            while max(cnt_lst) < times:
                times = times - 2
            for i in range(len(cnt_lst)):
                if cnt_lst[i] == times:
                    final_lst.append(final[i])
            max_num = max(final_lst)
            print(f'#{tc}', end=' ')
            for i in range(len(max_num)):
                print(max_num[i], end='')
            print()
        else:
            max_num = max(final)
            print(f'#{tc}', end=' ')
            for i in range(len(max_num)):
                print(max_num[i], end='')
            print()
    else:
        for i in range(len(cnt_lst)):
            if cnt_lst[i] == times:
                # print(cnt_lst[i])
                final_lst.append(final[i])
        # print(final_lst)
        max_num = max(final_lst)
        print(f'#{tc}', end=' ')
        for i in range(len(max_num)):
            print(max_num[i], end='')
        print()