T = int(input())
for tc in range(1, T+1):
    wd = input()
    wd_lst = []

    for i in wd:
        if len(wd_lst) == 0:
            wd_lst.append(i)
        elif len(wd_lst) != 0 and i != wd_lst[-1]:
            wd_lst.append(i)
        elif len(wd_lst) != 0 and wd_lst[-1] == i:
            wd_lst.pop()
    print(f'#{tc} {len(wd_lst)}')