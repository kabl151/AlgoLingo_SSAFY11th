import sys
input = sys.stdin.readline

for _ in range(4):
    lst = list(map(int,input().split()))
    L_lst = [0]*50002
    H_lst = [0]*50002
    rec_1 = lst[:4:]
    rec_2 = lst[4::]

    check_1 = 0
    check_2 = 0
    for i in range(rec_1[0], rec_1[2]+1):
        L_lst[i] += 1
    for i in range(rec_1[1], rec_1[3]+1):
        H_lst[i] += 1
    for i in range(rec_2[0], rec_2[2]+1):
        L_lst[i] += 1
    for i in range(rec_2[1], rec_2[3]+1):
        H_lst[i] += 1
    check_1 = L_lst.count(2)
    check_2 = H_lst.count(2)
    
    if check_1 == 0 or check_2 == 0:
        print('d')
    elif check_1 == 1 and check_2 == 1:
        print('c')
    elif check_1 == 1 and check_2 > 1:
        print('b')
    elif check_2 == 1 and check_1 > 1:
        print('b')
    elif check_1 > 1 and check_2 > 1:
        print('a')
