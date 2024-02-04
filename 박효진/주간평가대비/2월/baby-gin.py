
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    cnt_lst = [0] * 12
    input_num = int(input().strip())
    for i in range(6):
        cnt_lst[input_num % 10] += 1
        input_num //= 10
    k = 0
    triple = run = 0

    for j in range(10):
        if cnt_lst[j] == 6:
            cnt_lst[j] -= 6
            triple += 2

        if cnt_lst[j] >= 3:
            cnt_lst[j] -= 3
            triple += 1

    for k in range(10):
        if cnt_lst[k] == 2 and cnt_lst[k+1] == 2 and cnt_lst[k+2] == 2:
            cnt_lst[k] -= 2
            cnt_lst[k+1] -= 2
            cnt_lst[k+2] -= 2
            run += 2
        
        if cnt_lst[k] == 1 and cnt_lst[k+1] == 1 and cnt_lst[k+2] == 1:
            cnt_lst[k] -= 1
            cnt_lst[k+1] -= 1
            cnt_lst[k+2] -= 1
            run += 1

    if run + triple == 2:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')
