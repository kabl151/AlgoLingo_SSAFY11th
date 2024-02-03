T = int(input())
for tc in range(1, T+1):
    N_p, pa, pb = map(int, input().split())
    N_p_lst = [i for i in range(1, N_p + 1)]
    cnt_pa = 0
    cnt_pb = 0
    lft = 0
    rght = N_p - 1

    # a 탐색 횟수 측정
    while lft < rght:
        middle = int((lft + rght)/2)
        if N_p_lst[middle] == pa:
            break
        elif N_p_lst[middle] > pa:
            cnt_pa +=1
            rght = middle
        elif N_p_lst[middle] < pa:
            cnt_pa +=1            
            lft = middle
    # b 탐색 횟수 측정
    lft = 0
    rght = N_p - 1    
    while lft < rght:
        middle = int((lft + rght)/2)
        if N_p_lst[middle] == pb:
            break
        elif N_p_lst[middle] > pb:
            cnt_pb +=1
            rght = middle
        elif N_p_lst[middle] < pb:
            cnt_pb +=1            
            lft = middle
    if cnt_pa > cnt_pb:
        print(f'#{tc} B')
    elif cnt_pa < cnt_pb:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

