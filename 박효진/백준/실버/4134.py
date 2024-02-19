import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    test_num = int(input())
    while True:
        final_lst = []
        test_num += 1
        test_range = [x for x in range(test_num)]
        result_range = [True]*(test_num)
        result_range[0] = False
        result_range[1] = False
        for i in range(2, test_num):
            if result_range[i] == True:
                final_lst.append(test_range[i])
                for j in range(i, test_num, i):
                    result_range[j] = False
        if final_lst[-1] == test_num:
            break
    print(test_num)
