# import sys
# input = sys.stdin.readline
# import math

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     while True:
#         test_num = int(math.sqrt(N))
#         final_lst = []
#         lst = []
#         test_range = [x for x in range(test_num + 1)]
#         result_range = [True]*(test_num + 1)
#         result_range[0] = False
#         if test_num != 0:
#             result_range[1] = False
#         for i in range(2, test_num + 1):
#             if result_range[i] == True:
#                 final_lst.append(test_range[i])
#                 for j in range(i, test_num + 1, i):
#                     result_range[j] = False
#         for i in final_lst:
#             if N % i == 0:
#                 lst.append(i)
#         if len(lst) == 0 and N != 0 and N != 1:
#             print(N)
#             break
#         N += 1


# -----------------------------------------------------------------

import sys
input = sys.stdin.readline
import math

T = int(input())
for _ in range(T):
    N = int(input())
    if 0 <= N <= 2:
        print(2)
    elif N == 3:
        print(3)
    else:
        for i in range(N, 2*N):
            result = 0
            test_num = int(math.sqrt(i))
            for j in range(2, test_num+1):
                if i % j == 0:
                    result = 0
                    break
                else:
                    result = 1
            if result == 1:
                print(i)
                break