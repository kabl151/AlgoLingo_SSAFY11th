N = int(input())
cnt = 0
for i in range(1,N+1):
    wd = input()
    wd_lst = []
    for j in wd:
        if len(wd_lst) == 0:
            wd_lst.append(j)
        elif len(wd_lst) != 0 and j not in wd_lst:
            wd_lst.append(j)
        elif len(wd_lst) != 0 and wd_lst[-1] == j:
            wd_lst.append(j)
        elif len(wd_lst) != 0 and j in wd_lst and wd_lst[-1] != j:
            pass
    if len(wd_lst) == len(wd):
        cnt += 1
    else:
        pass
print(cnt)