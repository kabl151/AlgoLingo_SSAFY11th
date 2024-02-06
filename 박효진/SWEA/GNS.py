import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    num = arr[0]
    N = int(arr[1])
    input_lst = list(map(str, input().split()))
    num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_lst = []
    for i in num_lst:
        wd = input_lst.count(i)
        cnt_lst.append(wd)
    new_lst = []

    for i in range(10):
        for j in range(cnt_lst[i]):
            new_lst.append(num_lst[i])

    print(f'{num}')
    print(*new_lst)
