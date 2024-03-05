T = 10
for tc in range(1, T+1):
    arr = input().split()
    wd = str(arr[1])
    wd_lst = []
    for i in wd:
        if len(wd_lst) == 0:
            wd_lst.append(i)
        elif len(wd_lst) != 0 and i != wd_lst[-1]:
            wd_lst.append(i)
        elif len(wd_lst) != 0 and wd_lst[-1] == i:
            wd_lst.pop()
    result = ''.join(wd_lst)  
    print(f'#{tc} {result}')